from django.db import models
from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

# Create your models here.
class MetlabUserManager(UserManager):
	def _create_user(self, username, email, password, **extra_fields):
		if not username:
			raise ValueError("The given username must be set")
		if not email:
			raise ValueError("Email must be set")
		email = self.normalize_email(email)
			# Lookup the real model class from the global app registry so this
			# manager method can be used in migrations. This is fine because
			# managers are by definition working on the real model.
		GlobalUserModel = apps.get_model(
				self.model._meta.app_label, self.model._meta.object_name
			)
		username = GlobalUserModel.normalize_username(username)
		user = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_user(self, username, email, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", False)
		extra_fields.setdefault("is_superuser", False)
		return self._create_user(username, email, password, **extra_fields)
	def create_superuser(self, username, email, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		if extra_fields.get("is_staff") is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("Superuser must have is_superuser=True.")
		return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):


	email = models.EmailField(_("email address"), unique=True,)
	objects = MetlabUserManager()
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username"]
	
	def __str__(self):
		return self.email

# do not touch

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)
	url = models.URLField(max_length=80, null=True, blank=True)
	profile_info = models.CharField(max_length=150, null=True, blank=True)
	created = models.DateField(auto_now_add=True)
	picture = models.ImageField(upload_to='profile', blank=True, null=True, verbose_name='Picture')

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
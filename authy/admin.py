from django.contrib import admin
from authy.models import Profile, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# from datetime import timedelta
# from django.conf import settings
# from django.utils import timezone
# to clean up inactive users

# from .models import User
# User.objects.filter(
# is_active=False,
# date_joined__lt=timezone.now() -
# timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
# ).delete()

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
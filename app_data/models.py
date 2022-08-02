from django.db import models

# Create your models here.


















class Contact(models.Model):
	name = models.CharField(max_length=150, verbose_name='Name')
	email = models.EmailField()
	message_date = models.DateField()
	message = models.TextField(max_length=3000)

	def __str__(self):
		return self.name + self.email
		
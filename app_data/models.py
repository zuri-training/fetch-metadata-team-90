from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


from exiffield.fields import ExifField
from exiffield.getters import exifgetter
from .validators import validate_file_extension

from .filechecker import ContentTypeRestrictedFileField

# Create your models here.
UserModel = get_user_model()
content_types = [
    'application/json',
    'application/pdf',
    'audio/mpeg',
    'image/png',
    'image/jpeg',
    'image/jpg',
    'image/gif',
    'image/svg+xml',
    'text/csv',
    ]
max_upload_size = 5242880 #5mb

def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'

class FileUpload(models.Model):
    user = models.ForeignKey(UserModel, related_name='user_file', on_delete=models.CASCADE)
    file = ContentTypeRestrictedFileField(
        upload_to=user_directory_path,
        content_types=content_types,
        max_upload_size=max_upload_size,
        validators=[validate_file_extension]
    )
    file_name =  models.CharField( editable=False, max_length=100, blank=True, null=True)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
    exif = ExifField(
        source='file',
        denormalized_fields={
            'file_name': exifgetter('FileName'),
        },
    )
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.id})
    
    def __unicode__(self):
        return str(self.modefied)
    
    def __str__(self):
        return str(self.created)















class Contact(models.Model):
	name = models.CharField(max_length=150, verbose_name='Name')
	email = models.EmailField()
	message_date = models.DateField()
	message = models.TextField(max_length=3000)

	def __str__(self):
		return self.name + self.email
		
from django.contrib import admin
from .models import Contact, FileUpload
# Register your models here.
admin.site.register(Contact)
admin.site.register(FileUpload)
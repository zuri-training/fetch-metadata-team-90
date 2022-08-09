from django import forms
from .models import Contact, FileUpload

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'message')

class FileUploadForm(forms.ModelForm):
	class Meta:
		model = FileUpload
		fields = ['file']
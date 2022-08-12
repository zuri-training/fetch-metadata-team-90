from django import forms
from .models import FileUpload

class ContactForm(forms.Form):
	name = forms.CharField(max_length=150,)
	sender_email = forms.EmailField()
	subject = forms.CharField(max_length=150,)
	# message_date = forms.DateField()
	message = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={ 'rows':3, 'cols':5}))
	class Meta:
		fields = ['name', 'sender_email', 'subject', 'message']

class FileUploadForm(forms.ModelForm):
	class Meta:
		model = FileUpload
		fields = ['file']
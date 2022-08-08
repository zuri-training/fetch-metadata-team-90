from dataclasses import fields
from .models import FileContent
from django import forms

class FileContentForm(forms.ModelForm):
    class Meta:
        model = FileContent
        fields = ['file']

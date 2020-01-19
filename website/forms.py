from django import forms
from .models import Page

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['document']
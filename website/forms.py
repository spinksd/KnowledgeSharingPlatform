from django import forms
from dal import autocomplete
from .models import Page

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['document']

class CreateUpdatePageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'short_description', 'main_text', 'contacts', 'tags']
        widgets = {
            'contacts': autocomplete.ModelSelect2Multiple(url='contacts-autocomplete', attrs={
                # Set a placeholder
                'data-placeholder': 'Search contacts...',
                # Trigger autocompletion after a single character have been typed
                'data-minimum-input-length': 1,
            },)
        }
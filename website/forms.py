from django import forms
from django.contrib import messages
from dal import autocomplete
from .models import Page

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['document']

class CreateUpdatePageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'description', 'text', 'contacts', 'tags']
        widgets = {
            'contacts': autocomplete.ModelSelect2Multiple(url='contacts-autocomplete', attrs={
                # Set a placeholder
                'data-placeholder': 'Search contacts...',
                # Trigger autocompletion after a single character have been typed
                'data-minimum-input-length': 1,
            },),
        }
    
    def clean_data(self):
        # Ensure no more than 6 tags have been added to page
        tags = self.cleaned_data.get('tags', [])
        if len(tags) > 6:
            raise forms.ValidationError('Invalid number of tags. Can\'t have more than 6 tags!', code='invalid')

        # Ensure no more than 6 co tacts have been added to page
        contacts = self.cleaned_data.get('contacts', [])
        if len(contacts) > 6:
            raise forms.ValidationError('Invalid number of contacts. Can\'t have more than 6 contacts!', code='invalid')

        # The below should return the data of the current form
        # Such that the user's submitted data remains in the form (however, this currently doesn't seem to work)
        return self.cleaned_data

# This is a form to add autocomplete functionality to the contacts field in the advanced search on the home page
class AdvancedSearchForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['contacts', 'tags']
        widgets = {
            'contacts': autocomplete.ModelSelect2Multiple(url='contacts-autocomplete', attrs={
                # Set a placeholder
                'data-placeholder': 'Search contacts...',
                # Trigger autocompletion after a single character have been typed
                'data-minimum-input-length': 1,
            },),
        }
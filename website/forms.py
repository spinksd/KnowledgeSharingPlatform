from django import forms
from django.contrib import messages
from dal import autocomplete
from taggit.utils import edit_string_for_tags
from .models import Page

#class DocumentUploadForm(forms.ModelForm):
#    class Meta:
#        model = Page
#        fields = ['document']

class UploadFileForm(forms.Form):
    file = forms.FileField()

class CreateUpdatePageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'summary', 'main_text', 'document', 'tags', 'contacts']
        widgets = {
            'contacts': autocomplete.ModelSelect2Multiple(url='contacts-autocomplete', attrs={
                # Set a placeholder
                'data-placeholder': 'Search contacts...',
                # Trigger autocompletion after a single character have been typed
                'data-minimum-input-length': 1,
            },),
        }
    
    def clean_tags(self):
        # Ensure no more than 6 tags have been added to page
        tags = self.cleaned_data.get('tags', [])
        if len(tags) > 6:
            raise forms.ValidationError('Invalid number of tags. Can\'t have more than 6 tags!', code='invalid')
        return tags

    def clean_contacts(self):
        # Ensure no more than 6 co tacts have been added to page
        contacts = self.cleaned_data.get('contacts', [])
        if len(contacts) > 6:
            raise forms.ValidationError('Invalid number of contacts. Can\'t have more than 6 contacts!', code='invalid')
        elif len(contacts) < 1:
            raise forms.ValidationError('Invalid number of contacts. Must have at least 1 contact!', code='invalid')
        return contacts

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
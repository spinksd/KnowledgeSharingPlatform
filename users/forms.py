from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# UserCreationForm is a form provided by Django that has basic form inputs (Username, Password, password confirmation)
# It also ensures username and password conform to particular constrains (e.g. Password must be 8 chars and contain both alphabetical and numerical characters)
# Here I'm taking advantage of the default form, in addition to adding extra fields that I want on my registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Nested namespace for configurations
    class Meta:
        # Interact with User model - i.e. when running form.save() it will save to the 'User' model.
        model = User
        # Fields to display on the form in order specified
        fields = ['username', 'email', 'password1', 'password2']

# Allow user to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
        
    class Meta:
        model = User
        fields = ['username', 'email']
    
# Allow user to update profile image - this will be used in template with about function to look like one form
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['description', 'image']
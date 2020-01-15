
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        # Check if request method is a POST - i.e. User has previously filled in data but it doesn't match requirements - keep previously entered data in form fields.
        form = UserRegisterForm(request.POST)
        # Server-side check to see if form is valid (e.g. check passwords match, password is of sufficient complexity etc.)
        if form.is_valid():
            # Save form data (create user in database)
            # This is a great example of how Django can save a lot of time and effort as all I require here is 1 line of code.
            # Under the hood this method gets all the data values, connects to the db and writes all the data to the relevant table with the appropriate data.
            form.save()
            # Django stores valid form data in a python dictionary called 'cleaned_data'. Here I use the 'get' method to retrieve data from the dictionary and check the username is valid before confirming successful creation.
            username = form.cleaned_data.get('username')
            # Provide message to user telling them of successful user creation
            messages.success(request, f'Your account has been created! You are now able to login.')
            # Redirect user to sign-in page
            return redirect('login')
    else:
        # Else it's a GET request and is likely the first time the user has navigated to the page - show a blank form.
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Adding login_required decorator to the profile view - This forces a user to be logged in before being able to access this page.
@login_required
def profile(request):
    # POST method ran when user has potentially entered new data so pass in the POST data
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        # Profile also has image data attached to it, so make sure to load FILES data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # If data provided by user if valid, save form data to database (Update user's details)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            # Redirect user to profile page
            return redirect('profile')

    # Else it's a GET request, so load forms with user's current details populated
    else:
        # Print out forms - parameter specifies the instance that contains the user's current data (e.g. present user's current email to them in user update form)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)
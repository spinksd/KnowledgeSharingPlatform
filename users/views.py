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
            # Django stores valid form data in a python dictionary called 'cleaned_data'. Here we use the 'get' method to retrieve data from the dictionary.
            username = form.cleaned_data.get('username')
            # Provide message to user telling them of successful user creation
            messages.success(request, f'Your account has been created! You are now able to login.')
            # Redirect user to sign-in page
            return redirect('login')
    else:
        # Else it's a GET request and is likely the first time the user has navigated to the page - show a blank form.
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Adding login_required decorater to the profile view - This forces a user to be logged in before being able to access this page.
@login_required
def profile(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)
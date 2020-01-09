from django.db import models
from django.contrib.auth.models import User

# Inherit from Django model
class Profile(models.Model):
    # Make profile has one to one relationship with user. Additionally, delete profile if user gets deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Image field for user's profile picture. Defaults to blank user image if not set.
    image = models.ImageField(default='default_user.png', upload_to='profile_pics')

    # Here I define how I want the profile of a user to be presented - otherwise it would just present a profile object (and be difficult to understand what it relates to)
    def __str__(self):
        return f'{self.user.username} Profile'
import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Pillow is requirement for Django to process image fields so I already have this available
from PIL import Image

# Inherit from Django model
class Profile(models.Model):
    # Make profile has one to one relationship with user. Additionally, delete profile if user gets deleted.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Image field for user's profile picture. Defaults to blank user image if not set.
    image = models.ImageField(default='default_user.png', upload_to='profile_pics')

    # Here I define how I want the profile of a user to be presented - otherwise it would just present a profile object (and be difficult to understand what it relates to)
    def __str__(self):
        return f'{self.user.username} Profile'

    # Overwriting default save method in order to add rescaling of uploaded images to suitable icon size for platform
    # This saves both space on the platform, as well as loading times as the platform then doesn't have to pass a lot of data to the user (whereas for example, if it passed through a 4k image, it would be a lot of data)
    def save(self, *args, **kwargs):

        # Run cleanup of user's previous profile image (delete their old image as no longer in use)
        #previous_image = os.path.join(settings.MEDIA_ROOT, self.user.profile.image.name)
        #print('previous image path/name : ' + previous_image)
        #new_image = self.image.path
        #print('new image path/name : ' + new_image)
        # Check image is not the default image and that user has actually updated image (don't delete current image if user hasn't changed it)
        #if previous_image != "default.jpg" and previous_image != new_image:
        #    if os.path.exists(previous_image):
        #        os.remove(previous_image)
        #        print('image removed!')

        # Run default parent class save method
        super().save()
        # Custom addition of resizing image
        # Firstly, get the current image being uploaded (Done using the Image module provided by Pillow)
        with Image.open(self.image.path) as image:
            # Check if image is larger than a defined size, in this case I've chosen 300 x 300 as this reduces file sizes whilst mainting reasonable quality
            if image.height > 300 or image.width > 300:
                # Define size to resize image to
                output_size = (300, 300)
                # Set image to defined size
                image.thumbnail(output_size)
                # Overwrite uploaded image with re-sized image
                image.save(self.image.path)
# Importing a signal and a receiver
# As seen from path, the signal is one sent when the db gets a record added (an item gets saved)
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Also have a receiver which is a function that picks up on the signal and performs it's relevant task
from django.dispatch import receiver
from .models import Profile

# Create profile function to run every time a user is created
# When a user is saved, send post_save signal to this receiver
# post_save function passes 'instance' (in this case the user instance that has just been created) and 'created' parameters to the receiver
# kwargs simply accepts any additional parameters passed into the function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save/update user's profile if user's details get updated
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
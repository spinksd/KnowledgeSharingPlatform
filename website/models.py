from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create class/model for a page
class Page(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=300, blank=True)
    main_text = models.TextField()
    document = models.FileField(upload_to='documents/', blank=True)
    # Use taggit package to manage tags. Set blank=True such that the tags value can be blank.
    tags = TaggableManager(blank=True)
    # Can access contacts via .contacts.all() or .contacts.filter(...)
    contacts = models.ManyToManyField(User, related_name='contacts', blank=True)
    # Set date posted to current time/date
    date_posted = models.DateTimeField(default=timezone.now)
    # The below references the user who created the page, and if the user gets deleted, the author gets set to 'Deleted user'
    # This has been done as information on page may still be useful and therefore don't want to delete page if user gets deleted
    author = models.ForeignKey(User, on_delete=models.SET('Deleted User'))
    # Allow users to like pages
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    # Return the title of the page when querying it e.g. through python shell
    # Otherwise queryset returns data that could potentially be confusing
    # E.g. Creating a Page object with title 'Page 1':
    # Default representation: <QuerySet [<Page: Page object (1)>]>
    # Updated representation: <QuerySet [<Page: Page 1>]>
    def __str__(self):
        return self.title

    # Reverse simply returns the full url as a string - then I can use this for redirection (e.g. after user has created a page)
    def get_absolute_url(self):
        # Return the full url of the created page using it's primary key
        return reverse('published-page', kwargs={'pk': self.pk})

    # Function to return total number of likes of the page
    def total_likes(self):
        return self.likes.count()
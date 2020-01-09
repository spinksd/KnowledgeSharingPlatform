from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create class/model for a page
class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # The below references the user who created the page, and if the user gets deleted, the author gets set to 'Deleted user'
    # This has been done as information on page may still be useful and therefore don't want to delete page if user gets deleted
    author = models.ForeignKey(User, on_delete=models.SET('Deleted User'))

    # Return the title of the page when querying it e.g. through python shell
    # Otherwise queryset returns data that could potentially be confusing
    # E.g. Creating a Page object with title 'Page 1':
    # Default representation: <QuerySet [<Page: Page object (1)>]>
    # Updated representation: <QuerySet [<Page: Page 1>]>
    def __str__(self):
        return self.title
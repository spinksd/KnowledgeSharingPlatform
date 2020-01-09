from django.contrib import admin
from .models import Page

# This registers the page model with the admin interface provided by Django (at localhost:8000/admin)
admin.site.register(Page)
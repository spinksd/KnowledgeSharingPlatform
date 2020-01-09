from django.shortcuts import render
from .models import Page

def home(request):
    context = {
        'pages': Page.objects.all()
    }
    return render(request, 'website/home.html', context)

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})
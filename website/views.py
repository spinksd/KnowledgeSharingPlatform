from django.shortcuts import render

pages = [
    {
        'author': 'DSPINKS',
        'title': 'Page1',
        'content': 'First page content',
        'date_posted': 'January 6, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Page2',
        'content': 'Second page content',
        'date_posted': 'January 7, 2020'
    }
]

def home(request):
    context = {
        'pages': pages
    }
    return render(request, 'website/home.html', context)

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})
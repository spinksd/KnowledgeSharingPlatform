from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page

def home(request):
    context = {
        'pages': Page.objects.all()
    }
    return render(request, 'website/home.html', context)


# Inherits list view as page effectively has a 'list' of latest pages
class PageListView(ListView):
    model = Page
    # Update which template this list view interacts with
    template_name = 'website/home.html'
    context_object_name = 'pages'
    # Order pages so latest page is shown at top (This is done by the '-')
    ordering = ['-date_posted']

# Inherit from detail view as it provides the 'details' of the published page
class PageDetailView(DetailView):
    model = Page

# Inherit from LoginRequiredMixin such that the user is redirected to the login page when attempting to access this page when not logged in
# Also inherit from CreateView as this class is for creating a page
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    # Setting the fields the user will be able to edit when creating a page
    fields = ['title', 'content']

    # This specifies that the author of the page that is being created is the user who is currently logged in and submits the page creation
    def form_valid(self, form):
        # Specify author as current user (This is the neatest way of setting the author - if author is not specified then Django throws an integrity error as the NOT NULL constraint for author is failed)
        form.instance.author = self.request.user
        # Call original function to handle the rest of the processing
        return super().form_valid(form)

# Inherit from UpdateView as this class is for updating a page
# Also inherit from LoginRequiredMixin with addition of UserPassesTestMixin which allows me to add function to check user is author of the page
# The UserPassTestMixin allows me to add the test_func seen below - where I've added the author check functionality
class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    # Setting the fields the user will be able to edit when creating a page
    fields = ['title', 'content']

    # This specifies that the author of the page that is being created is the user who is currently logged in and submits the page creation
    def form_valid(self, form):
        # Specify author as current user (This is the neatest way of setting the author - if author is not specified then Django throws an integrity error as the NOT NULL constraint for author is failed)
        form.instance.author = self.request.user
        # Call original function to handle the rest of the processing
        return super().form_valid(form)
    
    def test_func(self):
        # Get current page user is trying to access the edit page for
        page = self.get_object()
        # Compare user who made request against author of the page
        if self.request.user == page.author:
            # If user who made request is the author, return true to allow user to edit the page
            return True
        else:
            return False

# Inherit from detail view as it provides the 'details' of the published page
class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    # Set success_url so that this is where the user is directed to (localhost:8000/) when a page is successfully deleted
    success_url = '/'
    
    # Same test function as above - check user attempting to delete page is the author of the page
    def test_func(self):
        # Get current page user is trying to access the edit page for
        page = self.get_object()
        # Compare user who made request against author of the page
        if self.request.user == page.author:
            # If user who made request is the author, return true to allow user to edit the page
            return True
        else:
            return False

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})
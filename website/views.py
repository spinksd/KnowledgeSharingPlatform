from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Page
from .forms import DocumentUploadForm

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'website/home.html'

# Inherits list view as page effectively has a 'list' of latest pages
class PageListView(LoginRequiredMixin, ListView):
    model = Page
    # Update which template this list view interacts with
    template_name = 'website/most_recent.html'
    context_object_name = 'pages'
    # Order pages so latest page is shown at top (This is done by the '-')
    ordering = ['-date_posted']
    # Defining the number of published pages that should be displayed on each page of the list view
    paginate_by = 5

# Inherits list view
class UserPageListView(LoginRequiredMixin, ListView):
    model = Page
    # Update which template this list view interacts with
    template_name = 'website/user_pages.html'
    context_object_name = 'pages'
    # Defining the number of published pages that should be displayed on each page of the list view
    paginate_by = 5

    def get_queryset(self):
        # Get user from User model where username is equal to the username in the url
        # This will 404 if user doesn't exist
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # Return pages where the user is the author, ordered by date_posted
        return Page.objects.filter(author=user).order_by('-date_posted')

# Inherit from detail view as it provides the 'details' of the published page
class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    is_liked = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page']
        if page.likes.filter(id=self.request.user.id).exists():
            context['is_liked'] = True
        return context

# Inherit from LoginRequiredMixin such that the user is redirected to the login page when attempting to access this page when not logged in
# https://docs.djangoproject.com/en/3.0/topics/auth/default/#the-loginrequired-mixin
# Also inherit from CreateView as this class is for creating a page
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    # Setting the fields the user will be able to edit when creating a page
    fields = ['title', 'short_description', 'main_text']

    # Get currently logged in user's profile image and description for sidebar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_img'] = self.request.user.profile.image.url
        context['profile_desc'] = self.request.user.profile.description
        return context

    # This specifies that the author of the page that is being created is the user who is currently logged in and submits the page creation
    def form_valid(self, form):
        # Specify author as current user (This is the neatest way of setting the author - if author is not specified then Django throws an integrity error as the NOT NULL constraint for author is failed)
        form.instance.author = self.request.user
        # Save form so tags can be added
        form.save()
        # Get tags from submitted form
        tags = self.request.POST.get('tag1') + ',' + self.request.POST.get('tag2') + ',' + self.request.POST.get('tag3') + ',' + self.request.POST.get('tag4') + ',' + self.request.POST.get('tag5') + ',' + self.request.POST.get('tag6')
        # Set page tags via so - removes all of the pages current tags then adds the new tags specified
        form.instance.tags.set(tags, clear=True)
        # Call original function to handle the rest of the processing
        return super().form_valid(form)
        

# Inherit from UpdateView as this class is for updating a page
# Also inherit from LoginRequiredMixin with addition of UserPassesTestMixin which allows me to add function to check user is author of the page
# The UserPassTestMixin allows me to add the test_func seen below - where I've added the author check functionality
class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    # Setting the fields the user will be able to edit when creating a page
    fields = ['title', 'short_description', 'main_text']

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

# Inherit from delete view as it provides delete functionality of a published page
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

class SearchResultsView(PageListView):
    template_name = 'website/search_results.html'
    ordering = []
    # redirect_field_name = 'redirect_to'

    # Use GET request for this so that searches can be shared between users
    # Filter on page titles
    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = Page.objects.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query) | Q(main_text__icontains=query)
        )
        return object_list


# Inherit from LoginRequiredMixin such that the user is redirected to the login page when attempting to access this page when not logged in
# Also inherit from CreateView as this class is for creating a page
class DocumentUploadView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'website/upload_document.html'
    fields = []

    def get(self, request):
        form = DocumentUploadForm()
        return render(request, 'website/upload_document.html', {'form': form})

    def post(self, request):
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign form to a temporary field
            temp = form.save(commit=False)
            # So that I can add user to the saved form in order to comply with the NOT NULL constraint on the author id of the page
            temp.author = request.user
            # Then save the form/page
            temp.save()
            return redirect('home')

# Inherits list view as page effectively has a 'list' of latest pages
class TopRatedListView(LoginRequiredMixin, ListView):
    model = Page
    # Update which template this list view interacts with
    template_name = 'website/top_rated.html'
    context_object_name = 'pages'
    # Defining the number of published pages that should be displayed on each page of the list view
    paginate_by = 5

    # Overwrite default queryset to get the total count of likes for each page, and then order by the most liked pages
    def get_queryset(self):
        return Page.objects.annotate(like_count=Count('likes')).order_by('-like_count')

    

def like_page(request, pk):
    # Get page object
    page = get_object_or_404(Page, id=pk)
    # Check if user has already liked the page. If so and they've clicked the button again - they're removing their like.
    if page.likes.filter(id=request.user.id).exists():
        page.likes.remove(request.user)
        is_liked = False
    # Else if user has not already liked the page, add a like from the user!
    else:
        page.likes.add(request.user)
        is_liked = True
    # Redirect user to the same published page
    return redirect('published-page', pk)

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})
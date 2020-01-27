from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView, UserPageListView, SearchResultsView, DocumentUploadView, HomePageView, TopRatedListView
from . import views

urlpatterns = [
    # Path below uses class view - by default searches for a template following the path: <app>/<model>_<viewtype>.html
    # The class view can overwrite the default path (as it does in the home view to 'templates/website/home.html')
    path('', HomePageView.as_view(), name='home'),
    # Brackets <> uses the 'pk' variable of the pages - Therefore, the first published page will have url localhost:8000/page/1
    # The 'pk' is a default attribute for the Django DetailView class and saves me having to pass along/translating a different variable name in numerous places
    path('page/<int:pk>/', PageDetailView.as_view(), name='published-page'),
    # Create and update view look for templates in location <app>/<model>_form.html
    path('create_page/', PageCreateView.as_view(), name='create-page'),
    path('page/<int:pk>/edit', PageUpdateView.as_view(), name='edit-page'),
    # Delete view looks for template in location <app>/<model>_confirm_delete.html
    path('page/<int:pk>/delete', PageDeleteView.as_view(), name='delete-page'),
    path('page/<int:pk>/like', views.like_page, name='like-page'),
    path('upload_document/', DocumentUploadView.as_view(), name='upload-document'),
    path('user/<str:username>', UserPageListView.as_view(), name='user-pages'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('top_rated/', TopRatedListView.as_view(), name='top-rated'),
    path('most_recent/', PageListView.as_view(), name='most-recent'),
    path('about/', views.about, name='about'),
]
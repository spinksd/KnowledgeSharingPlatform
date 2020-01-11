from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView
from . import views

urlpatterns = [
    #path('', views.home, name='website-home'),
    # Path below uses class view - by default searches for a template following the path: <app>/<model>_<viewtype>.html
    # The class view can overwrite the default path (as it does in the home view to 'templates/website/home.html')
    path('', PageListView.as_view(), name='website-home'),
    # Brackets <> uses the 'pk' variable of the pages - Therefore, the first published page will have url localhost:8000/page/1
    # The 'pk' is a default attribute for the Django DetailView class and saves me having to pass along/translating a different variable name in numerous places
    path('page/<int:pk>/', PageDetailView.as_view(), name='published-page'),
    # Create and update view look for templates in location <app>/<model>_form.html
    path('create_page/', PageCreateView.as_view(), name='create-page'),
    path('page/<int:pk>/edit', PageUpdateView.as_view(), name='edit-page'),
    # Delete view looks for template in location <app>/<model>_confirm_delete.html
    path('page/<int:pk>/delete', PageDeleteView.as_view(), name='delete-page'),
    path('about/', views.about, name='website-about'),
]
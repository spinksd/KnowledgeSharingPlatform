"""ksp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    # Important to have '/' after the url path, as then django will correctly interpret the url regardless of whether a user adds a slash on the end
    # I.e. Django will now resolve localhost:8000/register and localhost:8000/register/
    path('admin/', admin.site.urls),
    path('',  include('website.urls')),
    path('register/', user_views.register, name='register'),
    # Use of Django class based views to handle forms, logic and so on of authentication to platform
    # Works with the template I've created for login and logout which I've created in the 'users' app
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]

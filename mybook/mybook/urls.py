"""mybook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),

    #home
    #path('', views.home, name='home'),
    path('', views.loginuser, name='home'),

    #auth
    path('signupuser/', views.signupuser, name='signupuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),


    #Main Login Page
    path('mainlogin/', views.mainlogin, name='mainlogin'),



    path('makeentry/', views.makeentry, name='makeentry'),
    path('<slug:slug>', views.viewentry, name='viewentry'),
    path('<slug:slug>/edit', views.editentry, name='editentry'),
    path('<slug:slug>/delete', views.deleteentry, name='deleteentry'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

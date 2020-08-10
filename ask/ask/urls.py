"""ask URL Configuration

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
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^login/', views.test, name='login'),    
    url(r'^singup/', views.test, name='singup'),
    url(r'^question/<int:id>/', views.test, name='question'),
    url(r'^ask/', views.test, name='ask'),
    url(r'^popular/', views.test, name='popular'),
    url(r'^new/', views.test, name='new'),
]

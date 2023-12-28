"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.registerloginfunc,name='registerlogin'),
    path('forgot/',views.forgotpassfunc,name='forgotpass'),
    path('taskmanager/',views.taskmanagerfunc,name='taskmanager'),
    path('<int:id>/update',views.update,name='update'),
    path('<int:id>/delete',views.delete,name='delete')
]

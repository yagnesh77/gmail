from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
        path('', views.contact.as_view(), name='contact'),
   
]
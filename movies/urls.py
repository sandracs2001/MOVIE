from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('',views.home,name='home'),
]
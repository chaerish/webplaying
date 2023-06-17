from django.contrib import admin
from django.urls import path, include
from .views import login, signUp, find_id, find_pw

urlpatterns = [
    path('login', login ,name='login'),
    path('signup', signUp, name='signup'),
    path('findID', find_id, name='signup'),
    path('findPW', find_pw, name='signup'),
]
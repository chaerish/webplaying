from django.contrib import admin
from django.urls import path, include
from .views import login_view, signup, find_id, find_pw

app_name = 'home'

urlpatterns = [
    path('login', login_view ,name='login'),
    path('signup', signup, name='signup'),
    path('findID', find_id, name='findID'),
    path('findPW', find_pw, name='findPW'),
]
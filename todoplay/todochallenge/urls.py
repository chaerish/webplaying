from django.contrib import admin
from django.urls import path, include
from .views import challenge, challenge_detail

urlpatterns = [
    path('', challenge ,name='challenge'),
    path('1', challenge_detail, name='challenge_detail'),
]
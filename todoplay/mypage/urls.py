from django.contrib import admin
from django.urls import path, include
from .views import mypage, profile, info, friend, friend_management, friend_request, friend_accept

urlpatterns = [
    path('', mypage ,name='mypage'),
    path('profile', profile, name='profile'),
    path('info', info, name='info'),
    path('friend', friend, name='friend'),
    path('friend/request', friend_request, name='friend_request'),
    path('friend/accept', friend_accept, name='friend_accept'),
    path('friend/management', friend_management, name='friend_management'),

]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('month', views.month),
    path('day', views.day,name="day"),
    path('delete_item/<int:itempk>',views.delete_item)

]
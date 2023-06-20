from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'calendar'


urlpatterns = [
    path('month', views.month,name='month'),
    path('day', views.day, name="day"),
    path('delete_item/<int:itempk>',views.delete_item),
    # path('get-calendar-data', views.get_calendar_data),

]
from django.contrib import admin

from todocalendar.models import todoItem, Category

from todocalendar.models import calendarItem

# Register your models here.

admin.site.register(Category)
admin.site.register(todoItem)
admin.site.register(calendarItem)
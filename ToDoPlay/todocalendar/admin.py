from django.contrib import admin

from todocalendar.models import todoItem, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(todoItem)

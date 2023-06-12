from django.db import models



# Create your models here.

# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


# 투두아이템
class todoItem(models.Model):
    content = models.CharField(max_length=50, null=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.content}'




class calendarItem(models.Model):
    data = models.JSONField(null=True, blank=True)
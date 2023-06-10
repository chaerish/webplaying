import json

from django.shortcuts import render, redirect, get_object_or_404

from todocalendar.models import todoItem, Category


# Create your views here.

def month(request):
    item_list = todoItem.objects.select_related('category').order_by('-pk')
    context = {'item_list': item_list}
    return render(request, 'todocalendar/month.html', context)

def day(request):
    category_list = Category.objects.all()
    item_list = todoItem.objects.select_related('category').order_by('-pk')
    context = {'item_list': item_list,'category_list':category_list}

    if request.method=='POST':
        todo = request.POST.get('todo', '') #todo가져오기
        category_id = request.POST.get('category', '') #category가져옴
        category = Category.objects.get(id=category_id)
        todo_item = todoItem.objects.create(content=todo,category=category)
        return redirect('day')

    return render(request,'todocalendar/day.html',context)

def delete_item(request,itempk):
    item=todoItem.objects.get(pk=itempk)
    item.delete()
    return redirect('day')

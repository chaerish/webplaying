from django.shortcuts import render

from todocalendar.models import todoItem, Category


# Create your views here.

def month(request):
    item_list = todoItem.objects.select_related('category').order_by('-pk')
    context = {'item_list': item_list}
    return render(request, 'todocalendar/month.html', context)

def day(request):
    item_list = todoItem.objects.select_related('category').order_by('-pk')
    context = {'item_list': item_list}

    if request.method=='POST':
        todo = request.POST.get('todo', '') #todo가져오기
        category_id = request.POST.get('category', '') #category가져옴
        category = Category.objects.get(id=category_id)
        todo_item = todoItem.objects.create(content=todo)
        return render(request,'todocalendar/day.html')
    else:
        return render(request,'todocalendar/day.html',context)

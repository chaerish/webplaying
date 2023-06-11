import json
from email.quoprimime import unquote

from django.contrib.postgres import serializers
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from todocalendar.models import todoItem, Category


# Create your views here.

def month(request):
    item_list = todoItem.objects.select_related('category').order_by('-pk')
    context = {'item_list': item_list}

    return render(request, 'todocalendar/month.html', context)



# def day(request):
#     category_list = Category.objects.all()
#     item_list = todoItem.objects.select_related('category').order_by('-pk')
#     context = {'item_list': item_list, 'category_list': category_list}
#     # if request.method == 'GET':
#     #     query_params = request.GET.dict()
#     #     data = query_params.get('data')
#
#     return render(request, 'todocalendar/day.html', context)


# 삭제
def delete_item(request, itempk):
    item = todoItem.objects.get(pk=itempk)
    item.delete()
    return redirect('day')

#
# def get_calendar_data(request):
#     item_list = todoItem.objects.all()
#     data = [{
#         data,
#     },
#     ]
#     return JsonResponse(data, safe=False)

def day(request):
    category_list = Category.objects.all()
    item_list = todoItem.objects.select_related('category').order_by('-pk')
    context = {'item_list': item_list, 'category_list': category_list}


    if request.method == 'POST':
        todo = request.POST.get('todo', '')  # todo 가져오기
        category_id = request.POST.get('category', '')  # category 가져오기
        category = Category.objects.get(id=category_id)
        todo_item = todoItem.objects.create(content=todo, category=category)
        if 'data' in request.GET:
            date = request.GET.get('data','')
            data = {
                'date': date,
                'content': todo,
            }
            date_json = json.loads(data['date'])
            data['date'] = date_json['data']
            print(data)

        return redirect('day')  # POST 요청 후에는 day 뷰로 리다이렉트

    return render(request, 'todocalendar/day.html',context)

from django.shortcuts import render

# Create your views here.
def mypage(request):
    if request.method == 'GET':
        return render(request, 'mypage.html')

def profile(request):
    if request.method == 'GET':
        return render(request, 'manage_profile.html')

def info(request):
    if request.method == 'GET':
        return render(request, 'manage_info.html')

def friend(request):
    if request.method == 'GET':
        return render(request, 'manage_friend.html')

def friend_request(request):
    if request.method == 'GET':
        return render(request, 'friend_request.html')

def friend_accept(request):
    if request.method == 'GET':
        return render(request, 'friend_request_confirm.html')

def friend_management(request):
    if request.method == 'GET':
        return render(request, 'friend_list_manage.html')

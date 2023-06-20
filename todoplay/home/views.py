from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                nickname = request.POST["nickname"],
            )
            auth.login(request, user)  # 로그인
            return redirect('calendar:month')
        else:
            # form = UserForm()
            print(form.errors)
            return render(request,"signup.html",{"form":form})

    return render(request,"signup.html")

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username  # 세션에 사용자 저장
            return HttpResponse('로그인을 성공했습니다.')
        else:
            return HttpResponse('로그인에 실패했습니다.', status=400)


def logout_view(request):
    if request.method == 'POST':
        logout(request)  # 로그아웃
        request.session.pop('email', None)  # 세션에서 사용자 이메일 제거
        return redirect('/')


def find_id(request):
    if request.method == 'GET':
        return render(request, 'find_id.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        try:
            user = User.objects.get(email=email)
            nickname = user.nickname  # 사용자의 아이디
            # 아이디를 JSON 형식으로 응답
            return JsonResponse({'nickname': nickname})

        except User.DoesNotExist:
            # 사용자가 존재하지 않을 경우에는 에러 응답
            return JsonResponse({'error': '사용자를 찾을 수 없습니다.'}, status=400)


def find_pw(request):
    if request.method == 'GET':
        return render(request, 'find_pw.html')

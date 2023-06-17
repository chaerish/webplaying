from django.contrib.auth import get_user_model, authenticate, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

User = get_user_model()


# Create your views here.
def login(request):
    if request.method == 'GET':
        # GET 요청 처리
        # 필요한 로직을 수행하고, 데이터를 가져오는 등의 작업을 진행할 수 있습니다.

        # 예시: 데이터를 가져와서 context에 저장
        data = "Hello, World!"
        context = {'data': data}

        # HTML 템플릿 파일을 렌더링하여 HttpResponse 객체 반환
        return render(request, 'login.html', context)

    elif request.method == 'POST':
        email = request.POST.get('email', None)
        nickname = request.POST.get('nickname', None)
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)

        user = User.objects.create_user(email=email, password=password, nickname=nickname, name=name)
        user.profile_image = "default_profile.jpg"
        user.save()

        message = '회원가입을 성공했습니다.'
        return HttpResponse(message)


def signUp(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['email'] = user.email  # 세션에 사용자 이메일 저장
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

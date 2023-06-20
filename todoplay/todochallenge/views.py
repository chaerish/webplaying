from django.shortcuts import render

# Create your views here.
def challenge(request):
    if request.method == 'GET':
        return render(request, 'challenge.html')

def challenge_detail(request):
    if request.method == 'GET':
        return render(request, 'challenge_detail.html')

from urllib import response
from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'user/index.html')
    elif request.method == 'POST':
        username = request.POST.get('uid',None)
        password = request.POST.get('pwd',None)
        password2 = request.POST.get('repwd',None)
        
        if password != password2:
            return HttpResponse("비밀번호가 서로 맞지 않습니다.")
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return HttpResponse("이미 존재 하는 아이디 입니다.")
            else:
                UserModel.objects.create_user(username=username, password=password)
                return redirect('/')
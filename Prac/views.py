from django.http import HttpResponse
from django.shortcuts import render

def base(request):
    return HttpResponse("헬로우 장고")
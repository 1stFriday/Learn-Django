from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def greeting(requset, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def gaos(request):
    return HttpResponse("Hello, Gaos")

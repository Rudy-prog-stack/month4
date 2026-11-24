from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(r):
    return HttpResponse("Hello World!")

def greet(r, name):
    return HttpResponse(f"Привет, {name}! Добро пожаловать на сайт.")
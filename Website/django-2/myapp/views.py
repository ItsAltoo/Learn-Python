from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world")

def about(request):
    return HttpResponse("about page")

def home(request):
    return HttpResponse("home page")
# Create your views here.

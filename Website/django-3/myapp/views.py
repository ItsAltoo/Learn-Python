from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def button(request):
    return HttpResponse('<button style = "background-color:#212121;color:#eaeaea;font-weight:500px">Click me</button>')

def home(request):
    return render(request, 'index.html')
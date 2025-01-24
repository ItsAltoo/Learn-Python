from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse('Index Website'.upper())
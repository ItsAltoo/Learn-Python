from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Atomic',
        'heading':'Welcome to Atomic',
        'subheading':'this my atomic',
        'banner':'url("http://127.0.0.1:8000/static/img/BocchiTheRock.png");',
        'fontColor':'#FB4141'
    }
    return render(request,'index.html',context)
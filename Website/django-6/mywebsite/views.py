from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Atomic',
        'heading':'Welcome to Atomic',
        'subheading':'this my atomic'
    }
    return render(request,'index.html',context)
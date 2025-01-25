from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Home Page',
        'heading':'Welcome to my website',
        'page':'home'
    }
    return render(request,'index.html',context)
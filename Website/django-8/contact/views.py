from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'contact',
        'heading':'This Contact Me',
        'page':'contact'
    }
    return render(request,'index.html',context)
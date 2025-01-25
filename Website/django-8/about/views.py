from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'about',
        'heading':'This About Me',
        'page':'about'
    }
    return render(request,'index.html',context)
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Cek your weather'
    }
    return render(request,'index.html',context)
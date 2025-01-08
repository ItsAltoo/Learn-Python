from django.shortcuts import render

def index(request):
    context = {
        'title':'Portofolio',
        
    }
    return render(request,'index.html')
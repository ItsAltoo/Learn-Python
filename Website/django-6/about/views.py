from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'About Me',
        'heading' : 'This About Me Page',
        'subheading':'saya suka suka'
    }
    return render(request,'index.html',context)
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'About Me',
        'heading' : 'This About Me Page',
        'subheading':'saya suka suka',
        'banner':'url("http://127.0.0.1:8000/static/img/oceanGirl.jpg")',
        'fontColor':'#074799'
    }
    return render(request,'index.html',context)
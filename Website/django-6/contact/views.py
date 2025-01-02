from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title':'Contact Me..',
        'heading':'This Contact Page',
        'subheading':'qwerty@gmail.com',
        'banner':'url("http://127.0.0.1:8000/static/img/Nahida.jpg")',
        'fontColor':'#118B50'
    }
    return render(request,'index.html',context)

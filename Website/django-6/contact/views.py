from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title':'Contact Me..',
        'heading':'This Contact Page',
        'subheading':'qwerty@gmail.com'
    }
    return render(request,'index.html',context)

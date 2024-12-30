from django.shortcuts import render

# Create your views here.
def aboutPage(request):
    context = {
        'title' : 'About Us',
        'content' : 'Welcome to the About'
    }
    return render(request,"about/index.html",context)
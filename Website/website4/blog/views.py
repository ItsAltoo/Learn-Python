from django.shortcuts import render

# Create your views here.
def blogPage(request):
    return render(request,"blog.html")
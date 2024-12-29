from django.shortcuts import render

# Create your views here.
def aboutPage(request):
    return render(request,"about.html")
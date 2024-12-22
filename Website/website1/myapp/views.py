# filepath: /C:/Users/itsma/OneDrive/Documents/Project/Belajar/Python/Website/myproject1/myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse('<button style="background-color: blue; color: white;">Contact Us</button>')
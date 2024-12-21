# filepath: /C:/Users/itsma/OneDrive/Documents/Project/Belajar/Python/Website/myproject1/myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")
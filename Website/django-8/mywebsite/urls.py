from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('', include("home.urls")),
    path('contact/',include('contact.urls')),
    path('about/',include('about.urls'))
]

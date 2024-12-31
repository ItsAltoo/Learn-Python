from django.contrib import admin
from django.urls import path
from myapp import views  # Import views from myapp

urlpatterns = [
    path('', views.hello_world,name='hello_world'),  # Add a URL pattern for the hello_world view
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),  # Add a URL pattern for the home view
    path('about/', views.about, name='about'),  # Add a URL pattern for the about view
    path('contact/', views.contact, name='contact'),  # Add a URL pattern for the contact view
    
]

"""
URL configuration for website2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from myapp import views  # Import views from myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world, name='hello_world'),  # Add a URL pattern 
    path('about/', views.about, name='about'),  # Add a URL pattern
    path('home/', views.home, name='home'),  # Add a URL pattern
    #path('home/', views.about, name='about'),  # Add a URL pattern
    # mengapa path home dan about tidak bisa dijalankan bersamaan? karena pathnya sama 
    # dan akan menimbulkan error
    # maka dari itu kita harus mengganti pathnya
    # bagaimana jika kita ingin membuat path yang sama? kita bisa menggunakan include 
    # untuk mengatasi hal tersebut 
    # contohnya seperti ini
    # path('myapp/', include('myapp.urls'))
    # mengapa include not defined? karena kita belum mengimport include dari django.urls 
    # maka dari itu kita harus mengimport include terlebih dahulu 
    # dari django.urls 
    
    
    
    
    
]

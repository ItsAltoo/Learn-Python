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

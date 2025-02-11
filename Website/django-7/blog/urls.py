from django.urls import path

from . import views

urlpatterns = [
    path('',views.addMahasiswa,name='addMahasiswa'),
    path('delete/<int:id>/', views.deleteMahasiswa, name='deleteMahasiswa'),
]

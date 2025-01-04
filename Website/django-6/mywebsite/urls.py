from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('contact/',include('contact.urls')),
    path('about/',include('about.urls')),
    # ex: /5/results/
    path("<int:question_id>/results/", views.results, name="results"),
]

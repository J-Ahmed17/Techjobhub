from django.urls import include, path

from login import views



urlpatterns = [
   
    path("", views.loginaction),
    
]
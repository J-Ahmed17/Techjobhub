"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from signup.views import signaction
from login.views import loginaction
from . import index
urlpatterns = [
    path("admin/", admin.site.urls),
   #path("signup/", signaction, name="signup"),
   # path("login/", loginaction, name="login"),
   path("signup/", include('signup.urls')),
   #path("", include('signup.urls')),
    path("login/", include('login.urls')),
    
    path("F2/", index.authentication2, name="authentication2"),
    path("F6/", index.authentication6, name="authentication6"),
    path("", index.authentication3, name="authentication3"),
]

from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
<<<<<<< HEAD
    path('about',views.about,name="about"),
=======
>>>>>>> 049d486318770b0a0febe5699e65ef117c930f2c
]

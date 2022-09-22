from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('business', views.business),
    path('terrorism', views.terrorism),
    path('geopolitics', views.geopolitics),
    path('crime', views.crime),
    path('search', views.search),
    path('CNN', views.CNN),
    path('Bloomberg', views.Bloomberg),
    path('ANI', views.ANI),
    path('AiJazeera', views.AiJazeera),
    path('SCMP', views.SCMP)
]
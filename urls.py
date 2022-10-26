from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [

    path('hom', views.hom, name='hom'),
    path('addquestion', views.addquestion, name='addquestion'),
    
]

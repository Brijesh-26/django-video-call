
from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('register/', views.handleRegister),
    path('login/', views.handleLogin),
    path('home/', views.handleHome),
    path('meeting/', views.videocall, name= 'meeting'),
    path('joinmeeting/', views.join, name= 'joinmeeting'),    
    path('logout/', views.handleLogOut, name= 'handleLogOut')
]
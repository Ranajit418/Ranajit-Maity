"""rolebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from account import views


urlpatterns = [
    path('', views.index1, name='index1'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),

    path('addnews/', views.addnews, name='addnews'),
    path('allnews/', views.allnews, name='allnews'),
    path('newsdetails/<int:pk>/', views.newsdetails, name='newsdetails'),
    path('editnews/<int:pk>/', views.editnews, name='editnews'),
    path('deletenews/<int:pk>/', views.deletenews, name='deletenews'),
   
   
    

    path('index1/', views.index1, name='index1'),
    path('ece1/', views.ece1, name='ece1'),
    path('ee1/', views.ee1, name='ee1'),
    path('cse1/', views.cse1, name='cse1'),
    path('ce1/', views.ce1, name='ce1'),
    path('me1/', views.me1, name='me1'),
    path('about1/', views.about1, name='about1'),
    path('annualfest1/', views.annualfest1, name='annualfest1'),
    path('blood1/', views.blood1, name='blood1'),
    path('cdc1/', views.cdc1, name='cdc1'),  
    path('dkb1/', views.dkb1, name='dkb1'), 
    path('gargiday1/', views.gargiday1, name='gargiday1'), 
    path('infosis1/', views.infosis1, name='infosis1'), 
    path('leader1/', views.leader1, name='leader1'), 
    path('mining1/', views.mining1, name='mining1'), 
    path('pro1/', views.pro1, name='pro1'), 
    path('radio1/', views.radio1, name='radio1'), 
    path('ramt1/', views.ramt1, name='ramt1'), 
    path('science1/', views.science1, name='science1'), 
    path('sports1/', views.sports1, name='sports1'), 
    path('welder1/', views.welder1, name='welder1'), 
    path('women1/', views.women1, name='women1'), 
    path('work1/', views.work1, name='work1'),
    

           ]
         


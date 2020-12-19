from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('menu/', views.menu,name='menu'),
    path('eat/', views.eat,name='eat'),
    path('test/', views.test,name='test'),
    path('daietto/', views.daietto,name='daietto'),
    path('day1/', views.day1,name='day1'),
    path('day2/', views.day2,name='day2'),
    path('day3/', views.day3,name='day3'),
    path('afeat/', views.afeat,name='afeat'),
    path('touroku/', views.touroku,name='touroku'),
    path('ps1/', views.ps1,name='ps1'),
    path('ps2/', views.ps2,name='ps2'),
    path('ps3/', views.ps3,name='ps3'),

]
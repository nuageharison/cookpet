from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:page>', views.index,name='index'),
    path('okada:index2/',views.index2,name='index2'),
    path('okada:index3/',views.index3,name='index3'),

]








from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

     
    
   
    path('', views.stocks, name= 'stocks'),
    path('add_stocks/', views.add_stocks, name= 'add_stocks'),
    path('<int:id>/delete/', views.delete_stock),

]


from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

     
    
    path('', views.particulars, name= 'particulars'),
    path('menu/veg', views.veg, name= 'veg'),
    path('menu/egg', views.egg, name= 'egg'),
    path('menu/non_veg', views.non_veg, name= 'non_veg'),
    path('add_menu/', views.add_particulars, name= 'add_particulars'),
    path('menu/<int:id>/delete/', views.delete, name= 'delete'),
   

]

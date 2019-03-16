
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views




urlpatterns = [

     
    
   
    path('', views.customers, name= 'customers'),
    path('add/', views.add_customers, name= 'add_customers'),
    path('<int:id>/delete/',views.delete_customer_detail, name='del_cust'),
    path('<int:id>/delete1/',views.delete_customer, name='del_cust_main'),
    path('<int:id>/pdf/bill', views.get_bill, name= 'bill_pdf'),
    path('<int:id>/pdf/', views.get, name= 'pdf'),
    path('<int:id>/', views.dynamic_customers, name= 'cust_details'),

]

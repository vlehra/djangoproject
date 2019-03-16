from django.contrib import admin

# Register your models here.
from .models import Customer,Customer_detail

admin.site.register(Customer)
admin.site.register(Customer_detail)
from django.db import models
from datetime import datetime
from django.urls import reverse
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from products.models import Menu
from django.conf import settings
from django.db.models.signals import pre_save, post_save,m2m_changed
from django.contrib.auth.models import UserManager
# Create your models here.

class Customer(models.Model):
	name   = models.CharField(max_length = 35)
	mobile_number   = models.CharField(max_length=12, unique=True)
	address = models.TextField(blank=True, null=True)
	male = models.BooleanField(default=True)
	female = models.BooleanField(default=False)
	gym   = models.CharField(max_length=35)
	order  = models.ManyToManyField(Menu, related_name="order", blank=True)
	summary = models.CharField(max_length=200,blank=True)
	qty    = models.DecimalField(decimal_places=1, max_digits=100)
	total    = models.DecimalField(default=00, decimal_places=2, max_digits=10000)
	subtotal    = models.DecimalField(default=00, decimal_places=2, max_digits=10000)
	amount_paid =  models.DecimalField(decimal_places=2, max_digits=10000)
	date_cust = models.DateTimeField(default=datetime.now(), blank=True)
	
	def get_absolute_url(self):
		return reverse("cust_details", kwargs={"id": self.id})
	def delete_cust(self):
		return reverse("del_cust_main", kwargs={"id": self.id})

	def get_pdf(self):
		return reverse("pdf", kwargs={"id": self.id})

	def __str__(self):
		return self.name


def m2m_changed_cust1_receiver(sender, instance, action, *arg, **kwargs):
	print(action)
	if action == 'post_add' or 'post_remove' or 'post_clear':
		products = instance.order.all()
		total = 0
	for x in products:
		total += x.rate
	if instance.subtotal != total:
		instance.subtotal = total
	
		instance.save()
m2m_changed.connect(m2m_changed_cust1_receiver, sender=Customer.order.through)

def pre_save_cust1_receiver(sender, instance, *args, **kwargs):
	instance.total = instance.subtotal

pre_save.connect(pre_save_cust1_receiver, sender=Customer)
	
class Customer_detail(models.Model):
	mobile_number = models.CharField(max_length=13, unique=False)
	particular  = models.ManyToManyField(Menu, related_name="particular", blank=True)
	qty    = models.DecimalField(decimal_places=1, max_digits=100)
	subtotal    = models.DecimalField(default=00, decimal_places=2, max_digits=10000)
	total    = models.DecimalField(default=00, decimal_places=2, max_digits=10000)
	amount_paid =  models.DecimalField(decimal_places=2, max_digits=10000)
	date_cust = models.DateTimeField(default=datetime.now(), blank=True)
	
	
	def __str__(self):
		return str(self.id)

	def delete_cust_det(self):
		return reverse("del_cust", kwargs={"id": self.id})

	def get_pdf_bill(self):
		return reverse("bill_pdf", kwargs={"id": self.id})

	

def m2m_changed_cust_receiver(sender, instance, action, *arg, **kwargs):
	print(action)
	if action == 'post_add' or 'post_remove' or 'post_clear':
		products = instance.particular.all()
		total = 0
	for x in products:
		total += x.rate
	if instance.subtotal != total:
		instance.subtotal = total
	
		instance.save()
m2m_changed.connect(m2m_changed_cust_receiver, sender=Customer_detail.particular.through)

def pre_save_cust_receiver(sender, instance, *args, **kwargs):
	instance.total = instance.subtotal

pre_save.connect(pre_save_cust_receiver, sender=Customer_detail)




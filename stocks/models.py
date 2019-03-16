from django.db import models
from datetime import datetime



class Stock(models.Model):
	
	item    = models.CharField(max_length = 35)
	summary = models.TextField(blank=True, null=True)
	rate    = models.DecimalField(decimal_places=0, max_digits=6)
	qty    = models.DecimalField(decimal_places=2, max_digits=4)
	date = models.DateTimeField(default=datetime.now(), blank=True)



# Create your models here.

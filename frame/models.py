from django.db import models

# Create your models here.
class Feedback(models.Model):
	name   = models.CharField(max_length = 35)
	mobile_number   = models.CharField(max_length=12, unique=False)
	suggestions = models.TextField(blank=True, null=True)
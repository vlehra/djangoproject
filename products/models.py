from django.db import models

# Create your models here.
class Menu(models.Model):
	item    = models.CharField(max_length = 35)
	description = models.TextField(blank=True, null=True)
	rate    = models.DecimalField(decimal_places=2, max_digits=1000)
	veg     = models.BooleanField()
	egg     = models.BooleanField()
	non_veg     = models.BooleanField()

	def __str__(self):
		return self.item
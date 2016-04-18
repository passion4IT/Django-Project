from django.db import models


# model for category of the product
class Category(models.Model):
	name=models.CharField(max_length=30)
	
	def __str__(self):
		return self.name

#model for the detail information of the product
class Product(models.Model):
	category = models.ForeignKey(Category, null=True)
	name = models.CharField(max_length =120)
	productId = models.CharField(max_length=110)
	description = models.TextField()
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	manufacturer = models.CharField(max_length = 100)
	image = models.FileField(null=True, blank=True)

	class Meta:
		ordering = ["name", "productId"]

	def __str__(self):
		return self.name
	
	
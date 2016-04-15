from django.db import models



class Item(models.Model):
	name = models.CharField(max_length =120)
	productId = models.IntegerField()
	description = models.TextField()
	price = models.DecimalField(max_digits = 4, decimal_places = 2)
	manufacturer = models.CharField(max_length = 100)
	image = models.FileField(null=True, blank=True)

	class Meta:
		abstract = True

class Camera(Item):
	warranty = models.CharField(max_length=100)
	Zoomlens = models.CharField(max_length=50)
	wireless = models.BooleanField()

class Phone(Item):
	os = models.CharField(max_length = 50)
	screensize = models.CharField(max_length = 60)
	battery_life = models.CharField(max_length = 60)



def __str__(self):
	return self.name
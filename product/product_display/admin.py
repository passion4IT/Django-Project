from django.contrib import admin

from .models import Camera, Phone

class ModelAdmin(admin.ModelAdmin):
	list_display = ["name", "productId", "manufacturer"]
	list_filter = ["name", "productId", "price"]
	search_fields = ["name", "description","manufacturer", "productId"]
	

class CameraAdmin(ModelAdmin):
	class meta:
		model = Camera


class PhoneAdmin(ModelAdmin):
	class meta:
		model = Phone

admin.site.register(Camera, CameraAdmin)
admin.site.register(Phone, PhoneAdmin)
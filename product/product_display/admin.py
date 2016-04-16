from django.contrib import admin

from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	search_fields = ["name"]
	class Meta:
		model = Category
# 	list_display = ["name", "productId", "manufacturer"]
# 	list_filter = ["name", "productId", "price"]
# 	search_fields = ["name", "description","manufacturer", "productId"]
	

class ProductAdmin(admin.ModelAdmin):
	list_display = ["name", "manufacturer", "productId", "category"]
	list_filter = ["category"]
	search_fields = ["name", "productId"]
	class meta:
 		model = Product


# class PhoneAdmin(ModelAdmin):
# 	class meta:
# 		model = Phone

# admin.site.register(Camera, CameraAdmin)
# admin.site.register(Phone, PhoneAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
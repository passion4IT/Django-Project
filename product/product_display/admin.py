from django.contrib import admin

from .models import Category, Product


# Admin page modification for search option using name of the category
class CategoryAdmin(admin.ModelAdmin):
	search_fields = ["name"]
	class Meta:
		model = Category

	
# Admin page modification for search options, filter by fields with properties of the product
class ProductAdmin(admin.ModelAdmin):
	list_display = ["name", "manufacturer", "productId", "category"]
	list_filter = ["category"]
	search_fields = ["name", "productId"]
	class meta:
 		model = Product

# Registering extrafeatures of admin to the admin page of django 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
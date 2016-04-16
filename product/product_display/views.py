from django.shortcuts import render, get_object_or_404

# from .models import Item,Camera, Phone
from django.views.generic import TemplateView, DetailView
from .models import Category, Product

# def Pr_display(request):
# 	queryset = Camera.objects.all()
# 	queryset2 = Phone.objects.all()

# 	context = {
# 		"item" : queryset,
# 		"item2" : queryset2,
# 		"category": "Camera",
# 		"category2" : "SmartPhone"

# 	}

# 	return render(request, "base.html", context)



# def Category_product(request, id=None):
# 	instance = get_object_or_404(Item, id=id)


# 	return render(request, "category.html", {"instance": instance})
# 	


def product_display(request):
	instance = Product.objects.all()
	queryset = Category.objects.all()
	instance_context ={
		"product" : instance,
		"category": queryset

	}

	return render(request, "hello.html", instance_context)

class Category_display(DetailView):
	model = Category
	template = '/product/templates/category.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_category = context['object']
		context['Product'] = current_category.product_set.all()
		return context


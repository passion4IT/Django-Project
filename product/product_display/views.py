from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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

	query1= request.GET.get("search")
	query2= request.GET.get("searchId")

	if (query1):
		instance = instance.filter(name__icontains=query1)
		
	elif(query2):
		instance = instance.filter(productId__icontains=query2)

	else:
		instance = instance

	instance_context ={
		"product" : instance,
		"category": queryset

	}


	


	return render(request, "hello.html", instance_context)


def category_display(request, name):
	category_name = name
	cat_instance = Product.objects.filter(category__name=name)

	h_context = {
	"cat_context" : cat_instance,
	"cat_name" : category_name
	}

	return render(request, "category.html", h_context)

from django.shortcuts import render, get_object_or_404


from django.views.generic import TemplateView, DetailView
from .models import Category, Product



#View defined for the main product page 
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

# View defined for category-based product display plage
def category_display(request, name):
	category_name = name
	cat_instance = Product.objects.filter(category__name=name)

	h_context = {
	"cat_context" : cat_instance,
	"cat_name" : category_name
	}

	return render(request, "category.html", h_context)

from django.shortcuts import render

from .models import Camera, Phone


def Pr_display(request):
	queryset = Camera.objects.all()
	queryset2 = Phone.objects.all()

	context = {
		"item" : queryset,
		"item2" : queryset2,
		"category": "Camera",
		"category2" : "SmartPhone"

	}

	return render(request, "base.html", context)
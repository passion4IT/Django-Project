from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^',"product_display.views.Pr_display"),
    url(r'^camera/', "product_display.views."),
    url(r'^phone/', "product_display.views."),
    
]

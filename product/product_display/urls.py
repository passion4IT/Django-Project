from django.contrib import admin
from django.conf.urls import url


from . import views
from product_display.views import Category_display

urlpatterns = [
    
    url(r'^$',"product_display.views.product_display"),
    url(r'^(?P<pk>\d+)/$', Category_display.as_view(), name='category_details'),
    #url(r'^(?P<id>\d+)$', "product_display.views.category_display"),
    #url(r'^(?P<id>\d+)$', "product_display.views.Pr_display"),
    #url(r'^camera/(?P<id>\d+)$', "product_display.views.Pr_display"),
    #url(r'^phone/', "product_display.views."),
    
]

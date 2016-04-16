from django.contrib import admin
from django.conf.urls import url


from .views import(product_display, category_display)


urlpatterns = [
    
    url(r'^$',product_display),
    url(r'^(?P<name>.+)/$', category_display),
    #url(r'^product/(?P<id>\d+)/$', "product_display.views.product_detail", name="each_product"),
    #url(r'^(?P<id>\d+)$', "product_display.views.category_display"),
    #url(r'^(?P<id>\d+)$', "product_display.views.Pr_display"),
    #url(r'^camera/(?P<id>\d+)$', "product_display.views.Pr_display"),
    #url(r'^phone/', "product_display.views."),
    
]

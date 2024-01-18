from django.conf.urls import include, re_path
from .import views
from .views import  AbouttView
app_name = 'shop'
urlpatterns = [
    re_path(r'^$', views.product_list, name='product_list'),
    re_path(r'^(?P<pk>\d+)/$', views.product_list, name='product_list_with_pk'),
    re_path(r'^shopp/$', views.ShoppView , name='shopp'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    re_path(r'^about_uss/$',views.AbouttView, name='about_uss'),
    re_path(r'^contact_us/$', views.contact_us , name='contact_us'),
    re_path(r'^registershop/$', views.registershop, name='registershop'), 
    re_path(r'^search/$', views.search, name='search'),  
]

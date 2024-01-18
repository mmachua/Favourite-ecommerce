from django.conf.urls import url
from django.urls import include, re_path
from home.views import HomeView, AboutView# CreateView,ShopView,AboutView #, ContactView
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from home import views


app_name = 'home'
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'contact/$', views.contact, name='contact')
]
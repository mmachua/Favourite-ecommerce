from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from women import views
from django.conf.urls.static import static

urlpatterns = [
   path('cart/', include('cart.urls', namespace='cart')),
    path('home/',include('home.urls',namespace='home')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('shop/',include('shop.urls',namespace='shop')),   
#    path('register/',views.login_redirect, name='login_redirect'),
#    path('login/',include('login.urls',namespace='login')),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



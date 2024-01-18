#from .models import Product
#import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'name', ]
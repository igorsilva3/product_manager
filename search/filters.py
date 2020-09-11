import django_filters 
from product.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ['categorie']

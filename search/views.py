from django.shortcuts import render
from product.models import Product
from .filters import ProductFilter

# Create your views here.
def search(request):
    if request.method == 'GET':
        data = Product.objects.all()
        filter = ProductFilter(request.GET, queryset=data)

    return render(request, 'search/search.html', {'dataset': filter})
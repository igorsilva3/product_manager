from django.shortcuts import render
from product.models import Product
from .filters import ProductFilter
from django.core.paginator import Paginator

# Create your views here.
def search(request):
    if request.method == 'GET':
        data = Product.objects.all()
        filter = ProductFilter(request.GET, queryset=data)
        
        page = request.GET.get('page', 1)
        paginator = Paginator(filter.qs, 3)
        
        product = paginator.page(page)

    context = {
        'dataset': filter,
        'products': product
    }
    
    return render(request, 'search/search.html', context)
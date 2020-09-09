from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    if request.method == 'GET':
        # If there is result, returns all products registered
        product = Product.objects.all().order_by('name')
        
        # If there is no result, returns to the page not_found_products
        if not product.exists():
            return render(request, 'core/not_found_products.html')
        
    return render(request, 'core/index.html', {'dataset': product})
    
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        data = Product.objects.search(query)
        
        # Checks if the query did not return something and return page 404
        if not data.exists():
            return render(request, 'core/not_found_products.html')

    return render(request, 'core/index.html', {'dataset': data})
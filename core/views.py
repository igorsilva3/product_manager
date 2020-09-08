from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    if request.method == 'GET':
        # Checks if you have any products registered in the database, returning valores booleans
        product_exists = Product.objects.exists()
        
        # If there is no result, returns to the page not_found_products
        if product_exists == False:
            return render(request, 'core/not_found_products.html')
        
        # If there is result, returns all products registered
        product_exists = Product.objects.all()
    
    return render(request, 'core/index.html', {'dataset': product_exists})
    
        
    
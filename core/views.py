from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    if request.method == 'GET':
        data = Product.objects.all()
    
    return render(request, 'core/index.html', {'dataset': data})
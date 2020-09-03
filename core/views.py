from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    data = {}
    data['dataset'] = Product.objects.all()
    
    return render(request, 'core/index.html', data)
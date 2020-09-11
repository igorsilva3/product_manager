from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

# Create your views here.
def new(request):  
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None) 
            
        if form.is_valid(): 
            form.save() 
            return redirect('product:index')
    else:
        form = ProductForm(request.POST or None, request.FILES or None)
        
    return render(request, "product/new.html", {'form': form}) 

def list_product(request):
    if request.method == 'GET':
        product = Product.objects.exists()
        
        if not product:
            return render(request, 'product/not_found_products.html')
        
        # If there is result, returns all products registered
        product = Product.objects.all().order_by('name')
        
    return render(request, 'product/list_product.html', {'dataset': product})

def update(request, pk):
    product = get_object_or_404(Product, id=pk)  

    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        
    return render(request, 'product/change.html', {'form': form})

def delete(request, pk):
    product = get_object_or_404(Product, id=pk)  
    
    if request.method == 'POST':
        product.delete()
        return redirect('product:index')
    
    return render(request, 'product/delete.html', {'product': product})
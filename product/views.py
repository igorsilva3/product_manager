from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

# Create your views here.
def new(request):  
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None) 
            
        if form.is_valid(): 
            form.save() 
            return redirect('core:index')
    else:
        form = ProductForm(request.POST or None, request.FILES or None) 

    return render(request, "product/new.html", {'form': form}) 

def update(request, pk):
    product = get_object_or_404(Product, id=pk)  

    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
        
    return render(request, 'product/change.html', {'form': form})

def delete(request, pk):
    product = get_object_or_404(Product, id=pk)  
    
    if request.method == 'POST':
        product.delete()
        return redirect('core:index')
    
    return render(request, 'product/delete.html', {'product': product})
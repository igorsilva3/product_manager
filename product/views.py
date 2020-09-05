from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.
def new(request):  
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('core:index')
    else:
        form = ProductForm()

    return render(request, "product/new.html", {'form': form}) 

def update(request, pk):
    pass

def delete(request, pk):
    pass
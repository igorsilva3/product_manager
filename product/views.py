from django.shortcuts import render
from .forms import ProductForm

# Create your views here.
def new(request):
    data = {}
    
    form = ProductForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    data['form']= form 
    
    return render(request, "product/new.html", data) 

def update(request, pk):
    pass

def delete(request, pk):
    pass
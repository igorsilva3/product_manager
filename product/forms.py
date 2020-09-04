from django import forms
from .models import Product

# Create the form class.
class ProductForm(forms.ModelForm):
    """Form definition for Product."""

    class Meta:
        """Meta definition for Productform."""

        model = Product
        fields = [
            'name',
            'value',
            'description',
            'categorie',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'value': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'min': 0,
                    }
                ),
            'description': forms.Textarea(
                attrs={'class': 'form-control'}
                ),
            'categorie': forms.Select(
                attrs={'class': 'form-control col-md-6'}
                ),
        }
        


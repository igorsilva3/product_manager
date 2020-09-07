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
            'photo',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                    'id': 'inputName'
                    }
                ),
            'value': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Value',
                    'id': 'inputValue',
                    'min': '0',
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Description',
                    'id': 'inputDescription',
                    'rows': '3',
                    }
                ),
            'categorie': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'inputCategorie',
                    }
                ),
            'photo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                    'id': 'inputPhoto',
                    }
                ),
        }
        


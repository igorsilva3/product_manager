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


from django.db import models

# Create your models here.
class Categorie(models.Model):
    """Model definition for Categorie."""
    
    name = models.CharField(max_length=60, blank=False)
    created_date = models.DateField(auto_now_add = True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.name


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=60, blank=False)
    value = models.FloatField()
    description = models.TextField(blank=True)
    categorie =  models.CharField(max_length=60, blank=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

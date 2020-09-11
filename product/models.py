from django.db import models

# Create your models here.
class Categorie(models.Model):
    """Model definition for Categorie."""
    
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=60, blank=False)
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

    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=60, blank=False)
    brand = models.CharField("Brand", max_length=60, blank=True)
    value = models.FloatField("Value")
    description = models.TextField("Description", blank=True)
    categorie =  models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=False)
    photo = models.ImageField(upload_to='products', default='image_default.jpg')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name



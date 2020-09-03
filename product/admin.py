from django.contrib import admin
from .models import Categorie, Product

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date',)
    ordering = ['name']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'categorie', 'created_date', 'updated_date')
    ordering = ['name']

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Product, ProductAdmin)
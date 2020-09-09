from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query) | \
            models.Q(categorie__name__icontains=query)
        )
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.list_product, name='index'),
    path('product/new/', views.new, name='new'),
    path('product/change/<int:pk>/', views.update, name='change'),
    path('product/delete/<int:pk>/', views.delete, name='delete'),
]
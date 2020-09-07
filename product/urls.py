from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('change/<int:pk>/', views.update, name='change'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
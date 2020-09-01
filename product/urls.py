from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
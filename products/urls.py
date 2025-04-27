from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('welcome/', views.welcome, name='welcome'),
    path('products/', views.get_products, name='get_products'),  # All Products
    path('products/<int:id>/', views.get_product, name='get_product'),  # Single Product
    path('product/', views.create_product, name='create_product'),  # Create Product
    path('products/available/', views.get_available_products, name='get_available_products'),

]

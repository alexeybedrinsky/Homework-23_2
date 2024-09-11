from django.urls import path
from products.apps import ProductsConfig

from products.views import products_list, products_detail

app_name = ProductsConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:pk>/', products_detail, name='products_detail')
]
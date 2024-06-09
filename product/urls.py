from django.urls import path
from .views import getProduct, add_product, update_Product, delete_Product

urlpatterns = [
    path('getproduct/', getProduct, name="get product"),
    path('addproduct/', add_product, name="add product"),
    path('update_product/<int:pk>/', update_Product, name='update_product'),
    path('delete_product/<int:pk>/', delete_Product, name='delete_product')
]
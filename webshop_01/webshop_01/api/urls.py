from django.urls import path

from webshop_01.api.views import CartProducts, DeleteCartProduct

urlpatterns = [
    path('cart_add/', CartProducts.as_view(), name='cart_add'),
    path('cart_delete_product/', DeleteCartProduct.as_view(), name='delete_cart_product'),
]

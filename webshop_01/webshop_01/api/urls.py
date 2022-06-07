from django.urls import path

from webshop_01.api.views import CartProducts, DeleteCartProduct, AddProductToFavourites

urlpatterns = [
    path('cart_add/', CartProducts.as_view(), name='cart_add'),
    path('cart_delete_product/', DeleteCartProduct.as_view(), name='delete_cart_product'),
    path('add_to_favourites/', AddProductToFavourites.as_view(), name='add_product_favourites'),
]

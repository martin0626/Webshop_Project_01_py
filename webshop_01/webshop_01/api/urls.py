from django.urls import path

from webshop_01.api.views import CartProducts, DeleteCartProduct, AddProductToFavourites, ProductsInCart, \
    DeleteProductFromFavourites

urlpatterns = [
    path('cart_add/', CartProducts.as_view(), name='cart_add'),
    path('cart_delete_product/', DeleteCartProduct.as_view(), name='delete_cart_product'),
    path('add_to_favourites/', AddProductToFavourites.as_view(), name='add_product_favourites'),
    path('delete_from_favourites/', DeleteProductFromFavourites.as_view(), name='delete_product_favourites'),
    path('get_cart_items/', ProductsInCart.as_view(), name='get_cart_items'),
]

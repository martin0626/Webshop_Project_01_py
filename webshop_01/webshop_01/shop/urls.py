from django.urls import path

from webshop_01.shop.views import ShopView, ProductDetailsView, CartView

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('details/<int:pk>/', ProductDetailsView.as_view(), name='shop_details'),
]

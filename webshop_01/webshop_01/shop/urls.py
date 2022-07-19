from django.urls import path

from webshop_01.shop.views import ShopView, ProductDetailsView, CartView, PaymentView

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('<str:category>', ShopView.as_view(), name='shop'),
    path('<str:category>/<str:gender>', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('details/<str:slug>/', ProductDetailsView.as_view(), name='shop_details'),
]

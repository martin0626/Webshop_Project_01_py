from django.urls import path

from webshop_01.shop.views import ShopView, ProductDetailsView

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('details/<int:pk>/', ProductDetailsView.as_view(), name='shop_details'),
]

from django.urls import path

from webshop_01.shop.views import test_view, ShopView, ProductDetailsView

urlpatterns = [
    path('', test_view, name='test'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('details/<int:pk>/', ProductDetailsView.as_view(), name='shop_details'),
]

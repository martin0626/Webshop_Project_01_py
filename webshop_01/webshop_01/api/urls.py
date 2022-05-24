from django.urls import path

from webshop_01.api.views import CartProducts

urlpatterns = [
    path('cart_add/', CartProducts.as_view(), name='cart_add'),
]

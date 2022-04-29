from django.urls import path

from Webshop_01.shop.views import test_view

urlpatterns = [
    path('', test_view, name='test'),
]
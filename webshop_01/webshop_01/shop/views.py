from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from webshop_01.shop.models import Product


def test_view(request):
    return render(request, 'pages/shop-single.html')


class ShopView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'pages/shop-single.html'
    context_object_name = 'product'

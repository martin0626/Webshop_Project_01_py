from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from webshop_01.shop.models import Product, ProductGallery


class ShopView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cover_image = self.request
        return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'pages/shop-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        product = Product.objects.get(pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        photos = ProductGallery.objects.filter(product_id=self.kwargs['pk'])
        related_products = Product.objects.filter(category=product.category).exclude(id=self.kwargs['pk'])

        context['related_products'] = related_products[:4]
        context['photos'] = photos
        return context

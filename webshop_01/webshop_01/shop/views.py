from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

from webshop_01.shop.models import Product, ProductGallery, Category, Size


class ShopView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cover_image = self.request
        try:
            category_search = self.kwargs['category']
            if category_search == 'all':
                context['products'] = self.model.objects.all()
            else:
                context['products'] = self.model.objects.filter(category__slug=category_search)
            context['category'] = category_search

            try:
                gender_search = self.kwargs['gender']
                if category_search == 'all':
                    context['products'] = self.model.objects.filter(gender=gender_search)
                else:
                    context['products'] = self.model.objects.filter(gender=gender_search,
                                                                    category__slug=category_search)
            except KeyError:
                pass

        except KeyError:
            context['category'] = 'all'

        context['categories'] = Category.objects.filter(parent=None)
        return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'pages/shop-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        product = Product.objects.get(slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        photos = ProductGallery.objects.filter(product__slug=self.kwargs['slug'])
        related_products = Product.objects.filter(category=product.category).exclude(slug=self.kwargs['slug'])
        sizes = Size.objects.filter(product__slug=self.kwargs['slug'], quantity__gt=0)

        context['sizes'] = sizes
        context['related_products'] = related_products[:4]
        context['photos'] = photos[:3]
        return context


class CartView(TemplateView):
    template_name = 'pages/cart.html'


class PaymentView(TemplateView):
    template_name = 'pages/payment.html'


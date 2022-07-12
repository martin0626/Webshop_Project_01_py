from django.shortcuts import render
from django.views.generic import TemplateView

from webshop_01.text_pages.models import Banner


class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banners = Banner.objects.filter(is_active=True)
        context['banners'] = banners
        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'

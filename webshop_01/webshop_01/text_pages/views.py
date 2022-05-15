from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/index.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'

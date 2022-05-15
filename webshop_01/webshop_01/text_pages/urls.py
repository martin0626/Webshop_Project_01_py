from django.urls import path
from webshop_01.text_pages.views import HomeView, ContactView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]

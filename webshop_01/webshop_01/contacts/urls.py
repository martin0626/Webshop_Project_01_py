from django.urls import path

from webshop_01.contacts.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]
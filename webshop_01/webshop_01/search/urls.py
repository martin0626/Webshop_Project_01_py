from django.urls import path

from webshop_01.search.views import search_view

urlpatterns = [
    path('', search_view, name='search_view'),
]

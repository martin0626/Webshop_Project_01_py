from django.urls import path

from webshop_01.search.views import autocomplete, SearchView

urlpatterns = [
    path('', SearchView.as_view(), name='search_view'),
    path("autocomplete/", autocomplete, name='autocomplete'),
]

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from haystack.query import SearchQuerySet

from webshop_01.shop.models import Product


class SearchView(ListView):
    model = Product
    template_name = 'pages/search_results.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        result = SearchQuerySet().filter(text__startswith=query)
        return result


def autocomplete(request):

    if 'term' in request.GET:
        query = request.GET.get('term')
        qs = Product.objects.filter(title__startswith=query, is_active=True)
        titles = [r.title for r in qs]
        return JsonResponse(titles, safe=False)

    return render(request, 'pages/index.html')

from django.http import JsonResponse
from django.shortcuts import render
from haystack.query import SearchQuerySet

from webshop_01.shop.models import Product


def search_view(request, *args, **kwargs):
    query = request.GET.get('search')
    result = SearchQuerySet().filter(text__startswith=query)

    context = {
        'products': result,
    }

    return render(request, 'pages/search_results.html', context)


def autocomplete(request):

    if 'term' in request.GET:
        query = request.GET.get('term')
        qs = Product.objects.filter(title__startswith=query, is_active=True)
        titles = [r.title for r in qs]
        return JsonResponse(titles, safe=False)

    return render(request, 'pages/index.html')

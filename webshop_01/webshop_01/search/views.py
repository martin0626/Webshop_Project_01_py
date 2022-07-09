from django.shortcuts import render
from haystack.query import SearchQuerySet


def search_view(request, *args, **kwargs):
    query = request.GET.get('search')
    result = SearchQuerySet().filter(text=query)

    context = {
        'products': result,
    }

    return render(request, 'pages/search_results.html', context)

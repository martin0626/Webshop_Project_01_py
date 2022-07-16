from webshop_01.shop.models import Category


def category_processor(request):
    categories = Category.objects.all()
    return {
        'categories': categories,
    }

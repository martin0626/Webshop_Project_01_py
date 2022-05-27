from webshop_01.navigation.models import BaseNavigation


def nav_processor(request):
    base_navigation = BaseNavigation.objects.filter(is_active=True)
    return {
        'base_navigation': base_navigation,
    }


def cart_processor(request):
    cart_products = request.cart_products
    return {
        'cart_products': cart_products,
    }

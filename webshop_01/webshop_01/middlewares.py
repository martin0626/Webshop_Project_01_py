from webshop_01.shop.models import Product


def added_products_to_cart_middleware(get_response):
    def middleware(request):
        products_slugs = request.session.get('cart', [])
        cart = Product.objects.filter(slug__in=products_slugs)
        request.cart_products = cart
        request.cart_price = sum([product.price for product in cart])
        return get_response(request)
    return middleware
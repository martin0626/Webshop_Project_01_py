from webshop_01.navigation.models import BaseNavigation


def nav_processor(request):
    base_navigation = BaseNavigation.objects.filter(is_active=True)
    return {
        'base_navigation': base_navigation,
    }

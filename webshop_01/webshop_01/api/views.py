from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views
from rest_framework.response import Response


# TODO Finish 'Add product to cart'
from rest_framework.utils import json

from webshop_01.users.models import UserFavourites


@method_decorator(csrf_exempt, name='dispatch')
class CartProducts(views.APIView):

    def get(self, request):
        session = request.session.items()
        return Response(session)

    def post(self, request):
        slug = request.data.get('slug')
        cart_info = request.session.get('cart', [])
        if slug not in cart_info:
            cart_info.insert(0, slug)
            request.session['cart'] = cart_info
        print(cart_info)
        return Response()


@method_decorator(csrf_exempt, name='dispatch')
class DeleteCartProduct(views.APIView):

    def post(self, request):
        slug = request.data.get('slug')
        cart_info = request.session.get('cart', [])
        if slug in cart_info:
            cart_info.remove(slug)
            request.session['cart'] = cart_info
        print(cart_info)
        return Response()


class AddProductToFavourites(views.APIView):

    @staticmethod
    def get_favourites_count(user):
        favourites_count = UserFavourites.objects.filter(user=user).count()
        data = {
            'favourites_count': favourites_count,
        }
        return data

    def post(self, request):
        slug = request.data.get('slug')
        user = request.user
        is_favourite = UserFavourites.objects.filter(product=slug, user=user)
        if not is_favourite:
            favourite = UserFavourites(user=user, product=slug)
            favourite.save()

        return JsonResponse(self.get_favourites_count(user))

    def get(self, request):
        user = request.user
        return JsonResponse(self.get_favourites_count(user))

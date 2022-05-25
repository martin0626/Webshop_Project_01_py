from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views
from rest_framework.response import Response


# TODO Finish 'Add product to cart'
from rest_framework.utils import json


@method_decorator(csrf_exempt, name='dispatch')
class CartProducts(views.APIView):

    def get(self, request):
        session = request.session.items()
        return Response(session)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        slug = body['slug']
        cart_info = request.session.get('cart', [])
        if slug not in cart_info:
            cart_info.insert(0, slug)
            request.session['cart'] = cart_info
        print(cart_info)
        return Response()

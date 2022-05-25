from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response


# TODO Finish 'Add product to cart'
class CartProducts(views.APIView):

    def get(self, request):
        session = request.session.items()
        return Response(session)

    def post(self, request):
        pass

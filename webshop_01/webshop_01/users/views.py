from django.shortcuts import render, redirect
from django.views import View


class VerificationView(View):

    def get(self, request, uidb64, token):
        return 'success redirect'

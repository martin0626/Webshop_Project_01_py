from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.utils.encoding import force_str

from webshop_01.users.utils import token_generator

user = auth.get_user_model()


class UserLoginView(LoginView):
    # TODO Add template and form
    # form_class = LoginForm
    template_name = 'users/login.html'
    #
    # def get_success_url(self):
    #     return reverse_lazy('home')


class VerificationView(View):

    def get(self, request, uidb64, token):

        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            current_user = user.object.get(id=user_id)

            if not token_generator.check_token(current_user, token):
                return redirect('login')

            if current_user.is_active:
                return redirect('login')

            current_user.is_active = True
            current_user.save()

            return redirect('login')

        except Exception as ex:
            pass

        return 'success redirect'

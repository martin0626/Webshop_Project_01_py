from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.utils.encoding import force_str
from django.views.generic import CreateView, ListView

from webshop_01.shop.models import Product
from webshop_01.users.forms import RegisterForm, LoginForm
from webshop_01.users.models import UserFavourites
from webshop_01.users.utils import token_generator

user_model = auth.get_user_model()


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    model = user_model
    success_url = reverse_lazy('home')
    context_object_name = 'form'

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLogoutView(LogoutView):
    pass


class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            current_user = user_model.object.get(id=user_id)

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


class FavouritesView(ListView):
    model = UserFavourites
    template_name = 'pages/favourites.html'

    @staticmethod
    def get_slug_fields(favourite_products):
        return [p.product for p in favourite_products]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favourite_products_for_user = self.model.objects.filter(user=self.request.user)
        products = Product.objects.filter(slug__in=self.get_slug_fields(favourite_products_for_user))
        context['fav_products'] = products
        return context


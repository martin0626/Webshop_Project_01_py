from django.urls import path

from webshop_01.users.signals import profile_creator
from webshop_01.users.views import VerificationView, UserLoginView, UserRegisterView, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate')
]

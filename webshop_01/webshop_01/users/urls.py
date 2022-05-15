from django.urls import path

from webshop_01.users.signals import profile_creator
from webshop_01.users.views import VerificationView, UserLoginView

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate')
]

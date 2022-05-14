from django.urls import path

from webshop_01.users.signals import profile_creator
from webshop_01.users.views import VerificationView

urlpatterns = [
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate')
]

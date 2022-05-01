from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

import webshop_01.constants as constants
from webshop_01.users.managers import ShopUserManager


class ShopUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'
    object = ShopUserManager()


class Profile(models.Model):

    user = models.OneToOneField(
        ShopUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    phone = models.CharField(
        max_length=constants.PHONE_LEN,
        validators=[MinLengthValidator(constants.PHONE_LEN)],
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

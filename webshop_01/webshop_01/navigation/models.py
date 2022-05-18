from django.db import models
from django.urls import reverse

from webshop_01 import constants


class BaseNavigation(models.Model):
    URL_CHOICES = (
        ('shop', 'shop'),
        ('contact', 'contact'),
        ('about', 'about'),
        ('home', 'home'),
        ('login', 'login'),
        ('register', 'register'),
        ('logout', 'logout'),
    )

    title = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN
    )

    url_name = models.CharField(
        max_length=max([len(choice) for choice, _ in URL_CHOICES]),
        choices=URL_CHOICES,
    )

    slug_field = models.SlugField(
        unique=True,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    my_order = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False,
    )

    def get_absolute_url(self):
        return reverse(self.url_name)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['my_order']


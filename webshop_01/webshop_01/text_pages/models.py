from django.core.validators import MinValueValidator
from django.db import models

import webshop_01.constants as constants


class Banner(models.Model):
    title = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,

    )

    second_title = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,

        null=True,
        blank=True,
    )

    cover_image = models.ImageField(
        upload_to='banner_photos',
    )

    description = models.TextField(
        max_length=constants.TEXT_FIELD_DEFAULT_MAX_LEN
    )

    is_active = models.BooleanField(
        default=True,
    )

    slug_field = models.SlugField(
        unique=True,
    )

    my_order = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ['my_order']

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from djrichtextfield.models import RichTextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

import webshop_01.constants as constants


class Category(MPTTModel):
    # Helpful link: https://django-mptt.readthedocs.io/en/latest/tutorial.html
    name = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        unique=True,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['name']


class Product(models.Model):
    SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )

    title = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN
    )
    price = models.FloatField(
        validators=[MinValueValidator(constants.PRICE_DEFAULT_MIN_VALUE)]
    )

    rating = models.IntegerField(
        validators=[
            MinValueValidator(constants.RATING_DEFAULT_MIN_VALUE),
            MaxValueValidator(constants.RATING_DEFAULT_MAX_VALUE)
        ],
        default=0
    )

    brand = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN
    )

    description = RichTextField()

    specification = RichTextField()

    size = models.CharField(
        choices=SIZE_CHOICES,
        max_length=max([len(choice) for choice, _ in SIZE_CHOICES]),
    )

    quantity = models.PositiveIntegerField()

    is_active = models.BooleanField(
        default=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

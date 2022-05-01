from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from djrichtextfield.models import RichTextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

import webshop_01.constants as constants


class Category(MPTTModel):
    # Helpful link: https://django-mptt.readthedocs.io/en/latest/tutorial.html
    title = models.CharField(
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

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
    )
    logo = models.ImageField(
        upload_to="brand_photos",
        null=True,
    )

    def __str__(self):
        return self.name


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

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
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

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='product_photos'
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_cover = models.BooleanField(
        default=False,
    )

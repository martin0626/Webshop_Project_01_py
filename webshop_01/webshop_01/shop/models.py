from random import random, choice

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from djrichtextfield.models import RichTextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

import webshop_01.constants as constants

user = get_user_model()


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
    # TODO remove null = True on migration
    picture = models.ImageField(
        null=True,
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

    GENDER_CHOICES = (
        ('Men', 'Men'),
        ('Women', 'Women'),
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

    cover_image = models.ImageField(
        upload_to='product_photos',
        null=True,
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=max([len(choice) for choice, _ in GENDER_CHOICES]),
        default='Men',
    )

    def __str__(self):
        return self.title


class ProductGallery(models.Model):
    image = models.ImageField(
        upload_to='product_photos'
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_cover = models.BooleanField(
        default=False,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
    )


class Order(models.Model):
    STATUS_CHOICES = (
        ('In Process', 'In Process'),
        ('Accepted', 'Accepted'),
        ('Done', 'Done'),
    )
    order_number = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        unique=True,
        null=True,
    )

    description = models.TextField(
        max_length=constants.TEXT_FIELD_DEFAULT_MAX_LEN,
        blank=True,
    )

    order_status = models.CharField(
        max_length=max([len(choice) for choice, _ in STATUS_CHOICES]),
        choices=STATUS_CHOICES,
        default="In Process",
    )

    user = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # TODO REMOVE BLANK = TRUE
    products = models.ManyToManyField(
        Product,
        blank=True,
    )

    # TODO REMOVE BLANK = TRUE
    first_name = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        validators=[MinLengthValidator(5)],
        blank=True,
    )

    #TODO REMOVE BLANK = TRUE
    last_name = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        validators=[MinLengthValidator(5)],
        blank=True,
    )

    address = models.CharField(
        max_length=constants.CHAR_FIELD_DEFAULT_MAX_LEN,
        validators=[MinLengthValidator(5)],
        blank=True,
    )

    @staticmethod
    def number_generator():

        while True:
            number = ''.join([chr(choice(constants.ascii_codes_for_uppercase_letters__numbers)) for _ in range(constants.ORDER_NUMBER_SIZE)])
            is_exist = Order.objects.filter(order_number=number).exists()
            if not is_exist:
                return number

    def save(self, *args, **kwargs):
        # order_model = Order(
        #     order_number=self.number_generator(),
        #     description=self.description,
        #     order_status=self.order_status,
        #     user=self.user,
        #     products=self.products,
        #     first_name=self.first_name,
        #     last_name=self.last_name,
        #     address=self.address,
        #
        # )
        self.order_number = self.number_generator()
        super(Order, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # TODO Autogenerated order_number
    #     return super().save(*args, **kwargs)


class Size(models.Model):
    SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    size = models.CharField(
        max_length=max([len(c) for c, _ in SIZE_CHOICES]),
        choices=SIZE_CHOICES,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    quantity = models.IntegerField(
        default=0,
        validators=[MinLengthValidator(0)],
    )

    def __str__(self):
        return f"{self.size} - {self.product.slug}"

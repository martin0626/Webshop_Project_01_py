from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from webshop_01.shop.models import Category, Product, ProductGallery, Brand


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("title",)}
    mptt_level_indent = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product']

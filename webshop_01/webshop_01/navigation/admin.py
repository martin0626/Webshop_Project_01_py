from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from webshop_01.navigation.models import BaseNavigation


@admin.register(BaseNavigation)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'my_order']
    prepopulated_fields = {"slug_field": ("title",)}

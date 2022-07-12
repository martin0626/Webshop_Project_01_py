from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from webshop_01.text_pages.models import Banner


@admin.register(Banner)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'my_order']
    prepopulated_fields = {"slug_field": ("title",)}

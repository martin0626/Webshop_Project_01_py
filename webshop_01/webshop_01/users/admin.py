from django.contrib import admin

from webshop_01.users.models import ShopUser, Profile, UserFavourites


@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(UserFavourites)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['product']

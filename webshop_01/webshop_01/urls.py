from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webshop_01.text_pages.urls')),
    path('shop/', include('webshop_01.shop.urls')),
    path('users/', include('webshop_01.users.urls')),
    path('contacts/', include('webshop_01.contacts.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webshop_01.text_pages.urls')),
    path('shop/', include('webshop_01.shop.urls')),
    path('users/', include('webshop_01.users.urls')),
    path('contacts/', include('webshop_01.contacts.urls')),
    path('contacts/', include('webshop_01.api.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

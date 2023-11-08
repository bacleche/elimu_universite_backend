"""elimu_universite URL Configuration """

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from elimu_universite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

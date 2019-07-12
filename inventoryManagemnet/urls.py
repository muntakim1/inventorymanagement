from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import management
urlpatterns = [
    path('',include('management.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

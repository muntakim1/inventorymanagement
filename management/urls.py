from django.urls import path,include
from django.contrib import admin
from .router import router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    path('auth/',include('djoser.urls.jwt')),
]

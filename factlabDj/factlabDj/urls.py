from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('home.urls')),
    path("",include('dbupdate.urls')),
    path("",include('dbfetch.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

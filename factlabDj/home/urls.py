from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .import views as v

urlpatterns = [
    path('home/', v.home),
    path('', v.home)

]
urlpatterns += staticfiles_urlpatterns()

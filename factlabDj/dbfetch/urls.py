from django.contrib import admin
from django.urls import path
from .import views as v


urlpatterns = [
    path('fetch', v.dbfetch),
    path('searchrecord',v.fetchrecord)
]

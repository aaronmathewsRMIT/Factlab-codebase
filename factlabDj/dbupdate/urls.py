from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('update', v.dbupdate),
    path('addrecord',v.add_record)
]

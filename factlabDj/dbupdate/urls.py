from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('update', v.dbupdate),
    path('addrecord',v.add_record),
    path('modify', v.dbmodify),
    path('updaterecord', v.update_record),
    path('testapi/', v.update_record),
]

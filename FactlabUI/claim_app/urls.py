from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.home),
    path("home/",views.home, name = 'home'),
    path('update', views.dbupdate),
    path('fetch', views.dbfetch),
    path('a', views.dbsearchNew),
    path('addrecord',views.add_record),
    path('searchrecord',views.fetchrecord),
    path('login/', views.loginPage, name= 'login'),  
    path('logout/', views.logoutUser, name= 'logout'),
]

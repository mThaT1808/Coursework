from django.urls import path, include
from django.contrib import admin
from journal import views


urlpatterns = [
    path('', views.main),
    path('teachers/', views.teachers),
    path('groups/', views.groups),
]
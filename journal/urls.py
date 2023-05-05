from django.urls import path, include
from django.contrib import admin
from journal import views


urlpatterns = [
    path('', views.main),
    path('teachers/', views.teachers),
    path('groups/', views.groups),
    path('groups/timetable/<int:id>/', views.timetable_by_group),
    path('groups/subjects/<int:id>/', views.journal),
    path('subjects/', views.subjects_list),
    ]
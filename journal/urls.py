from django.urls import path, include
from journal import views


urlpatterns = [
    path('', views.main),
    path('accounts/', include('django.contrib.auth.urls')),
]
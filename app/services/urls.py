from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
from . import views


urlpatterns = [
    path('services/', views.ServicesRead.as_view(), name='services'),
    path('services/add/', views.ServicesCreate.as_view(), name='services_add'),
    path('services/add/<int:pk>/', views.ServicesUpdate.as_view(), name='services_update'),
    path('services/delete/<int:pk>/', views.ServicesDelete.as_view(), name='delete'),
]

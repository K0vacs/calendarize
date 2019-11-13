from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = 'services'

urlpatterns = [
    path('services/', views.ServiceTable.as_view(), name='services'),
    path('services/add/', views.ServiceCreate.as_view(), name='service_add'),
    path('services/add/<int:pk>/', views.ServiceUpdate.as_view(), name='service_update'),
    path('services/delete/<int:pk>/', views.ServiceDelete.as_view(), name='delete'),
]

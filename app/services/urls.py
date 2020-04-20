from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/', views.ServiceTable.as_view(), name='services'),
    path('services/add/', views.ServiceCreate.as_view(), name='service_add'),
    path('services/add/<int:pk>/', views.ServiceUpdate.as_view(), name='service_update'),
    path('services/delete/<int:pk>/', views.ServiceDelete.as_view(), name='service_delete'),
]

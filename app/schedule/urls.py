from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'schedule'

urlpatterns = [
    path('schedule/', views.ScheduleTable.as_view(), name='schedule'),
    # path('equipment/add/', views.EquipmentCreate.as_view(), name='equipment_add'),
    # path('equipment/add/<int:pk>/', views.EquipmentUpdate.as_view(), name='equipment_update'),
    # path('equipment/delete/<int:pk>/', views.EquipmentDelete.as_view(), name='equipment_delete'),
]
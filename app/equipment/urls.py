from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'equipment'

urlpatterns = [
    path('equipment/', views.EquipmentTable.as_view(), name='equipment'),
    path('equipment/add/', views.EquipmentCreate.as_view(), name='equipment_add'),
    path('equipment/add/<int:pk>/', views.EquipmentUpdate.as_view(), name='equipment_update'),
    path('equipment/delete/<int:pk>/', views.EquipmentDelete.as_view(), name='equipment_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

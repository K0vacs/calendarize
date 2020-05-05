from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Naming the module urls
app_name = 'equipment'

# Defining the urls in the module
urlpatterns = [
    path('equipment/', login_required(views.EquipmentTable.as_view()), name='equipment'),
    path('equipment/add/', login_required(views.EquipmentCreate.as_view()), name='equipment_add'),
    path('equipment/add/<int:pk>/', login_required(views.EquipmentUpdate.as_view()), name='equipment_update'),
    path('equipment/delete/<int:pk>/', login_required(views.EquipmentDelete.as_view()), name='equipment_delete'),
]

# This enables static and media urls to resolve correctly
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

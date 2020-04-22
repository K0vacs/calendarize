from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/', login_required(views.ServiceTable.as_view()), name='services'),
    path('services/add/', login_required(views.ServiceCreate.as_view()), name='service_add'),
    path('services/add/<int:pk>/', login_required(views.ServiceUpdate.as_view()), name='service_update'),
    path('services/delete/<int:pk>/', login_required(views.ServiceDelete.as_view()), name='service_delete'),
]

from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('staff/', views.StaffTable.as_view(), name='staff'),
    path('staff/add/', views.StaffCreate.as_view(), name='staff_add'),
    path('staff/add/<int:pk>/', views.StaffUpdate.as_view(), name='staff_update'),
    path('staff/delete/<int:pk>/', views.StaffDelete.as_view(), name='staff_delete'),
]
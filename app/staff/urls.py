from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

# Naming the module urls
app_name = 'staff'

# Defining the urls in the module
urlpatterns = [
    path('staff/', login_required(views.StaffTable.as_view()), name='staff'),
    path('staff/add/', login_required(views.StaffCreate.as_view()), name='staff_add'),
    path('staff/add/<int:pk>/', login_required(views.StaffUpdate.as_view()), name='staff_update'),
    path('staff/delete/<int:pk>/', login_required(views.StaffDelete.as_view()), name='staff_delete'),
]
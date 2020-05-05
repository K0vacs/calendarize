from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

# Naming the module urls
app_name = 'bookings'

# Defining the urls in the module
urlpatterns = [
    path('bookings/', login_required(views.BookingsTable.as_view()), name='bookings'),
    path('bookings/add/', login_required(views.BookingsCreate.as_view()), name='bookings_add'),
    path('bookings/add/<int:pk>/', login_required(views.BookingsUpdate.as_view()), name='bookings_update'),
    path('bookings/delete/<int:pk>/', login_required(views.BookingsDelete.as_view()), name='bookings_delete'),
    path('customer-status/delete/<int:pk>/', login_required(views.CustomerStatusDelete.as_view()), name='customerstatus_delete'),
]
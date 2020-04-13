from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'bookings'

urlpatterns = [
    path('bookings/', views.BookingsTable.as_view(), name='bookings'),
    # path('bookings/', views.BookingsTable.as_view(), name='bookings'),
    path('bookings/add/', views.BookingsCreate.as_view(), name='bookings_add'),
    path('bookings/add/<int:pk>/', views.BookingsUpdate.as_view(), name='bookings_update'),
    path('bookings/delete/<int:pk>/', views.BookingsDelete.as_view(), name='bookings_delete'),
    path('customer-status/delete/<int:pk>/', views.CustomerStatusDelete.as_view(), name='customerstatus_delete'),

    # path('customerstatus/delete/<int:pk>/', views.CustomerPriceDelete.as_view(), name='customerstatus_delete'),
]
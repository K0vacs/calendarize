from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('customers/', views.CustomersRead.as_view(), name='customers'),
    path('customers/add/', views.CustomersCreate.as_view(), name='customers_add'),
    path('customers/add/<int:pk>/', views.CustomersUpdate.as_view(), name='customers_update'),
    path('customers/delete/<int:pk>/', views.CustomersDelete.as_view(), name='customers_delete'),

    # path('test/', views.create_book_with_authors, name='book'),
    path('test/', views.CreateBookClass.as_view(), name='book'),
    path('test/<pk>/', views.CreateBookClass.as_view(), name='bookid'),
]
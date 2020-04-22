from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('customers/', login_required(views.CustomerTable.as_view()), name='customers'),
    path('customers/add/', login_required(views.CustomerCreate.as_view()), name='customer_add'),
    path('customers/add/<int:pk>/', login_required(views.customerupdate), name='customer_update'),
    path('customers/delete/<int:pk>/', login_required(views.CustomerDelete.as_view()), name='customer_delete'),
    path('customerprice/delete/<int:pk>/', login_required(views.CustomerPriceDelete.as_view()), name='customerprice_delete'),
]

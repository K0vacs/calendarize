from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('overview/', views.overview, name='overview'),
    # path('services/', views.services, name='services'),
    path('services/', views.ServicesRead.as_view(), name='services'),
    path('<model>/add-new/', views.ServicesCreate.as_view(), name='add_new'),
    path('<model>/add-new/<int:pk>/', views.ServicesUpdate.as_view(), name='update'),
    path('<model>/delete/<int:pk>/', views.ServicesDelete.as_view(), name='delete'),
]

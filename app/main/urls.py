from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.home, name='home'),
    path('overview/', views.overview, name='overview'),

    path('', include('bookings.urls')),
    path('', include('services.urls')),
    path('', include('customers.urls')),
    path('', include('equipment.urls')),
    path('', include('staff.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('bookings.urls')),
    path('', include('services.urls')),
    path('', include('customers.urls')),
    path('', include('equipment.urls')),
    path('', include('staff.urls')),
    path('', include('schedule.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

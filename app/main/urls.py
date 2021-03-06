from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

# These are all the urls for the application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', views.HomePage.as_view(), name='home'),
    path('payment/<message>', views.PaymentSubmission.as_view(), name='payment'),
    path('contact/<message>', views.FormSubmission.as_view(), name='contact'),

    # These urls are included from other modules
    path('', include('bookings.urls')),
    path('', include('services.urls')),
    path('', include('customers.urls')),
    path('', include('equipment.urls')),
    path('', include('staff.urls')),
    path('', include('schedule.urls')),
]

# This enables static and media urls to resolve correctly
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('form-submission/<message>', views.FormSubmission.as_view(), name='contact'),
    path('charge/<message>', views.PaymentSubmission.as_view(), name='charge'),
    path('', views.HomePageView.as_view(), name='home'),
]
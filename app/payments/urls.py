from django.urls import path
from . import views

urlpatterns = [
    path('form-submission/<message>', views.FormSuccess.as_view(), name='contact'),
    path('charge/', views.charge, name='charge'),
    path('', views.HomePageView.as_view(), name='home'),
]
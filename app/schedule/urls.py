from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('schedule/', views.ScheduleTable.as_view(), name='schedule'),
    path('schedule/<date>', views.ScheduleTable.as_view(), name='schedule_date'),
]
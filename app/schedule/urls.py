from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', login_required(views.ScheduleTable.as_view()), name='home'),
    path('schedule/', login_required(views.ScheduleTable.as_view()), name='schedule'),
    path('schedule/<date>', login_required(views.ScheduleTable.as_view()), name='schedule_date'),
]
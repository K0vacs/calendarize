from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

# Naming the module urls
app_name = 'schedule'

# Defining the urls in the module
urlpatterns = [
    path('schedule/', login_required(views.ScheduleTable.as_view()), name='schedule'),
    path('schedule/<date>', login_required(views.ScheduleTable.as_view()), name='schedule_date'),
]
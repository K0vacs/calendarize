from django.shortcuts import render
from django.views.generic import ListView
from bookings.models import Bookings
from staff.models import Staff
from equipment.models import Equipment
from datetime import date

class ScheduleTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.

    model = Bookings
    template_name = 'schedule.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        context['metas'] = self.model._meta.fields
        context['staff'] = Staff.objects.all().values('username', 'image')
        context['today'] = date.today().strftime("%d %B %Y")
        # test = Equipment.objects.values()
        # test = list(test)
        # test[0]['boom'] = 'Paw'
        context['equipment'] = Equipment.objects.values()
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list(
            'id',
            'date',
            'start_time',
            'end_time',
            'service_id__name',
            'equipment_id__name',
            'staff_id__username',
        )

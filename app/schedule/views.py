from django.shortcuts import render
from django.views.generic import ListView
from bookings.models import Bookings
from staff.models import Staff
from equipment.models import Equipment
from .forms import *
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

class ScheduleTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.
    # form_class = searchForm
    model = Bookings
    template_name = 'schedule.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        context['metas'] = self.model._meta.fields
        context['staff'] = Staff.objects.all().values('username', 'image')
        try: 
            pk_date = self.kwargs["date"]
        except:    
            pk_date = datetime.date.today().strftime("%d-%m-%Y")

        context['date'] = datetime.datetime.strptime(pk_date, "%d-%m-%Y").strftime("%d %B %Y")
        context['test'] = searchForm()
        context['test1'] = self.request.POST.get('search_date') or "None"
        context['equipment'] = Equipment.objects.values()
        return context

    # def get_paginate_by(self, queryset):
    #     items_per_page = self.request.POST.get('results') or 10
    #     return items_per_page

    def get_queryset(self):
        try: 
            pk_date =  self.kwargs["date"]
        except:    
            pk_date = datetime.date.today().strftime("%d-%m-%Y")

        db_date = datetime.datetime.strptime(pk_date, "%d-%m-%Y").strftime("%d/%m/%Y")
        return self.model.objects.filter(date=db_date).values_list(
            'id',
            'date',
            'start_time',
            'end_time',
            'service_id__name',
            'equipment_id__name',
            'staff_id__username',
        )

    def post(self, request, *args, **kwargs):
        search_date   = searchForm(request.POST or None)
        if search_date.is_valid():
            return self.form_valid(search_date)
        else:
            # context = self.get_context_data(**kwargs) 
            return self.form_invalid(search_date)
            # return HttpResponseRedirect(reverse('schedule:schedule_date', kwargs = { 'date': request.POST['search_date'] }))
        # return HttpResponseRedirect(reverse('schedule:schedule'))

    def form_valid(self, search_date):
        date = search_date.cleaned_data['search_date']
        date = datetime.datetime.strptime(date, "%d/%m/%Y").strftime('%d-%m-%Y')
        return HttpResponseRedirect(reverse('schedule:schedule_date', kwargs = { 'date': date }))

    def form_invalid(self, search_date):
        # return HttpResponseRedirect(reverse('schedule:schedule'))
        # context = self.get_context_data()
        # context = self.get_context_data(**kwargs) 
        # context["test"] = search_date
        # self.get_context_data(**ScheduleTable.kargs)
        try: 
            pk_date =  self.kwargs["date"]
        except:    
            pk_date = datetime.date.today().strftime("%d-%m-%Y")

        db_date = datetime.datetime.strptime(pk_date, "%d-%m-%Y").strftime("%d/%m/%Y")
        
        context = { 
            "test": search_date,
            "date": datetime.datetime.strptime(pk_date, "%d-%m-%Y").strftime("%d %B %Y"),
        }
        return render(self.request, self.template_name, context)
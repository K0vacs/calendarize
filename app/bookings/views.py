from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib import messages
from .models import *
# from .utils import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.core import serializers
import numpy as np

class BookingsTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.

    model = Bookings
    template_name = 'bookings.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        context['metas'] = self.model._meta.fields
        context['form'] = BookingsStaticForm(self.request.POST)
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list()

class BookingsCreate(SuccessMessageMixin, CreateView):

    form_class = BookingsStaticForm
    template_name = 'bookings_add.html'
    success_message = "%(id)s was created successfully"

    def get_context_data(self, **kwargs):
        context                   = super().get_context_data(**kwargs)
        context['date_formset']   = BookingsDateFormset(
            queryset=Bookings.objects.none(), 
            prefix='bookings'
        )
        context['status_formset'] = CustomerStatusModelFormset(
            queryset=CustomerStatus.objects.none(), 
            prefix='customer'
        )
        return context

    def post(self, request, *args, **kwargs):
        date_formset   = BookingsDateFormset(request.POST or None, prefix='bookings')
        status_formset = CustomerStatusModelFormset(request.POST, prefix='customer')
        booking_form   = BookingsStaticForm(request.POST)
        
        if date_formset.is_valid() and status_formset.is_valid() and booking_form.is_valid():
            return self.form_valid(date_formset, status_formset, booking_form)
        else:
            return self.form_invalid(date_formset, status_formset, booking_form)
    
    def form_valid(self, date_formset, status_formset, booking_form):
        booking = booking_form.save(commit=False)
        ids = []
        
        for form in date_formset.save(commit=False):
            form.service    = booking.service
            form.equipment  = booking.equipment
            form.staff      = booking.staff
            response        = form.save()
            ids.append(form.pk)

        repeatedIds = np.tile(ids, len(ids))

        for id, status in zip(repeatedIds, status_formset.save(commit=False)):
                status.booking_id = id
                status.save()

        if(len(date_formset) == 1):
            return HttpResponseRedirect(reverse('bookings:bookings_update', kwargs = { 'pk': str(repeatedIds) }))
        return HttpResponseRedirect(reverse('bookings:bookings'))

    def form_invalid(self, date_formset, status_formset, booking_form):
        context = {
            "date_formset": date_formset,
            "status_formset": status_formset,
            "form": booking_form,
        }

        return render(self.request, self.template_name, context)


class BookingsUpdate(SuccessMessageMixin, UpdateView):
    form_class = BookingsStaticForm
    template_name = 'bookings_add.html'
    success_message = "%(date)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = Bookings.objects.filter(pk=self.kwargs['pk']).values_list()
        d = t[0][1]
        booking        = BookingsStaticForm(d)
        customerstatus = CustomerStatusModelFormset(queryset=CustomerStatus.objects.filter(booking_id=self.kwargs['pk']))
        context['formset'] = customerstatus
        context['booking'] =  d
        return context

    def get_queryset(self):
        query = Bookings.objects.filter(pk=self.kwargs['pk'])
        return query

class BookingsDelete(DeleteView):
    # Delete individual Booking records in a modal

    model = Bookings

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
    
    def get_success_url(self):
        # status = CustomerStatus.objects.get(customer_id=self.object.pk)
        # status.delete()
        return reverse_lazy('bookings:bookings')
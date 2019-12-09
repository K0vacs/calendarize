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

class BookingsTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.

    model = Bookings
    template_name = 'bookings.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        context['metas'] = self.model._meta.fields
        context['form'] = BookingsForm(self.request.POST)
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list()

class BookingsCreate(SuccessMessageMixin, CreateView):

    form_class = BookingsForm
    template_name = 'bookings_add.html'
    success_message = "%(id)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customerstatus = CustomerStatusModelFormset(queryset=CustomerStatus.objects.none())
        context['formset'] = customerstatus
        return context

    def post(self, request, *args, **kwargs):
        bookingform = BookingsForm(request.POST)
        formset = CustomerStatusModelFormset(request.POST)
        
        if bookingform.is_valid() and formset.is_valid():
            return self.form_valid(bookingform, formset)
    
    def form_valid(self, bookingform, formset):
        response = bookingform.save()
        for item in formset.save(commit=False):
            item.booking_id = response.pk
            item.save()
        return HttpResponseRedirect(reverse('bookings:bookings_update', kwargs = { 'pk': response.pk }))

class BookingsUpdate(SuccessMessageMixin, UpdateView):
    form_class = BookingsForm
    template_name = 'bookings_add.html'
    success_message = "%(date)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = Bookings.objects.filter(pk=self.kwargs['pk']).values_list()
        d = t[0][1]
        booking        = BookingsForm(d)
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
        CustomerStatus.objects.filter(customer_id=self.object.pk).delete()
        return reverse_lazy('bookings:bookings')
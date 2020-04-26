from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BookingsStaticForm, CustomerStatusForm, customer_status_formset
from .models import Bookings, CustomerStatus
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime



class BookingsTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.

    model = Bookings
    template_name = 'bookings.html'
    context_object_name = 'pages'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Bookings"
        context['metas'] = self.model._meta.fields
        return context

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

class BookingsCreate(SuccessMessageMixin, CreateView):

    form_class = BookingsStaticForm
    template_name = 'bookings_add.html'
    success_message = "%(id)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "New"
        context["title"] = "Booking"
        context['status_formset'] = customer_status_formset(1)(
            queryset=CustomerStatus.objects.none(), 
            prefix='customer'
        )
        return context

    def post(self, request, *args, **kwargs):
        status_formset = customer_status_formset(1)(request.POST, prefix='customer')
        booking_form   = BookingsStaticForm(request.POST)
        
        if status_formset.is_valid() and booking_form.is_valid():
            return self.form_valid(status_formset, booking_form)
        else:
            return self.form_invalid(date_formset, status_formset, booking_form)
    
    def form_valid(self, status_formset, booking_form):
        booking = booking_form.save()

        for status in status_formset.save(commit=False):  
            status.booking_id = booking.pk
            status.save()

        return HttpResponseRedirect(reverse('bookings:bookings_update', kwargs = { 'pk': booking.pk }))

    def form_invalid(self, status_formset, booking_form):
        context = {
            "status_formset": status_formset,
            "form": booking_form,
        }

        return render(self.request, self.template_name, context)


class BookingsUpdate(SuccessMessageMixin, UpdateView):
    form_class = BookingsStaticForm
    template_name = 'bookings_add.html'
    success_message = "Your booking was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = "Update"
        context["title"] = "Booking"
        context['field_status'] = 'disabled'
        context['status_formset'] = customer_status_formset(1)(
                                        queryset=CustomerStatus.objects.filter(
                                        booking_id=self.kwargs['pk']
                                        ),
                                        prefix='customer'
                                    )

        return context

    def get_queryset(self):
        query = Bookings.objects.filter(pk=self.kwargs['pk'])
        return query

    def post(self, request, *args, **kwargs):
        status_formset = customer_status_formset(1)(request.POST, prefix='customer')
        query = Bookings.objects.get(pk=self.kwargs['pk'])
        booking_form = BookingsStaticForm(request.POST, instance=query)
        
        if status_formset.is_valid() and booking_form.is_valid():
            return self.form_valid(status_formset, booking_form)
        else:
            return self.form_invalid(status_formset, booking_form)
    
    def form_valid(self, status_formset, booking_form):      
        booking = booking_form.save()
        
        for status in status_formset.save(commit=False):
            status.booking_id = self.kwargs['pk']
            status.save()

        return HttpResponseRedirect(reverse('bookings:bookings_update', kwargs = { 'pk': self.kwargs['pk'] }))

    def form_invalid(self, status_formset, booking_form):
        context = {
            "status_formset": status_formset,
            "form": booking_form,
        }

        return render(self.request, self.template_name, context)

class BookingsDelete(DeleteView):
    # Delete individual Booking records in a modal

    model = Bookings

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('bookings:bookings')

class CustomerStatusDelete(DeleteView):
    # Delete individual Customer Status records through an Ajax request

    model = CustomerStatus

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
    
    def get_success_url(self):
        return reverse('bookings:bookings')
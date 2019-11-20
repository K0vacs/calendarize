from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import *
from .utils import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# from django.contrib.messages import constants as messages

# MESSAGE_TAGS = {
#     messages.INFO: 'danger',
#     50: 'critical',
# }

class CustomerTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.

    model = Customers
    template_name = 'customers.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        context['metas'] = self.model._meta.fields
        context['form'] = CustomersForm(self.request.POST)
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list()

class CustomerCreate(SuccessMessageMixin, CreateView):
    # This class creates a Customers and CustomersPrice database record(s) when the form is submitted.

    template_name = 'customers/add.html'
    form_class = CustomersPriceForm
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super(CustomerCreate, self).get_context_data(**kwargs)
        customerprice = ServiceModelFormset(queryset=CustomersPrice.objects.none())
        context['formset'] = customerprice
        context['customer_form'] = CustomersForm()
        return context

    def post(self, request, *args, **kwargs):
        formset = ServiceModelFormset(request.POST)
        customerform = CustomersForm(request.POST)
        if formset.is_valid() and customerform.is_valid():
            return self.form_valid(formset, customerform)

    def form_valid(self, formset, customerform):
        response = customerform.save()
        for item in formset.save(commit=False):
            item.customer_id = response.pk
            item.save()
        return HttpResponseRedirect(reverse('customers:customer_add', kwargs={'pk': response.pk}))

def customerupdate(request, pk):
    # Read and Update individual Customer records in a form

    if request.method == 'GET':
        customerform = CustomersForm(instance=Customers.objects.get(pk=pk))
        formset = ServiceModelFormset(queryset=CustomersPrice.objects.filter(customer_id=pk))
    elif request.method == 'POST':
        customerform = CustomersForm(request.POST or None, instance=Customers.objects.get(pk=pk))
        formset = ServiceModelFormset(request.POST)

        if formset.is_valid() and customerform.is_valid():
            obj= customerform.save(commit= False)
            obj.save()

            itemlist = []
            for item in formset.save(commit=False):    
                itemlist.append(item.services_id)
                item.customer_id = pk
            
            if len(itemlist) != len(set(itemlist)):
                messages.success(request, "Duplicate service prices are not allowed", extra_tags="danger")
            else:
                messages.success(request, "Customer was updated successfully")
                formset.save()
            
            return redirect('customers:customer_update', pk=pk)
    return render(request, 'customers/add.html', {
        'formset': formset,
        'customer_form': customerform,
        })

class CustomerDelete(DeleteView):
    # Delete individual Customer records in a modal

    model = Customers

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
    
    def get_success_url(self):
        CustomersPrice.objects.filter(customer_id=self.object.pk).delete()
        return reverse_lazy('customers:customers')

class CustomerPriceDelete(DeleteView):
    # Delete individual Customer Price records in the repeater field

    model = CustomersPrice

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)

    def get_success_url(self):
        return reverse_lazy('customers:customer_update', kwargs={'pk': self.object.customer_id})
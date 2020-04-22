from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Staff
from .forms import StaffForm, StaffUpdateForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

class StaffTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.

    model = Staff
    template_name = 'staff.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exclude'] = [
            'id', 
            'password', 
            'last_login', 
            'is_superuser', 
            'is_staff', 
            'is_active', 
            'date_joined',
            'image',
        ]
        context['metas'] = self.model._meta.fields
        context['title'] = "Staff"
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list(
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'cell'
            )

class StaffCreate(SuccessMessageMixin, CreateView):
    form_class = StaffForm
    template_name = 'staff_add.html'
    success_message = "%(username)s was created successfully"

    def get_success_url(self):
        return reverse_lazy('staff:staff_update', kwargs = { 'pk': self.object.id })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "New"
        context['title'] = "Staff"
        return context

class StaffUpdate(SuccessMessageMixin, UpdateView):
    form_class = StaffUpdateForm
    template_name = 'staff_add.html'
    success_message = "%(username)s was created successfully"

    def get_queryset(self):
        query = Staff.objects.filter(pk=self.kwargs['pk'])
        return query

    def post(self, request, *args, **kwargs):
        instance = Staff.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Update"
        context['title'] = "Staff"
        return context

class StaffDelete(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff:staff')

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)

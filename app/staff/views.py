from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

class StaffTable(ListView):
    # This class reads from the Customers database records and displays the returned data in a table.

    model = Staff
    template_name = 'staff.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
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
        context['form'] = StaffForm(self.request.POST)
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list('id', 'username', 'first_name', 'last_name', 'email', 'cell')

class StaffCreate(SuccessMessageMixin, CreateView):
    form_class = StaffForm
    template_name = 'staff_add.html'
    success_message = "%(username)s was created successfully"

    def get_success_url(self):
        return reverse_lazy('staff:staff_update', kwargs = { 'pk': self.object.id })

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.url = "hello"
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return self.form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        return context

class StaffUpdate(UpdateView):
    form_class = StaffUpdateForm
    template_name = 'staff_add.html'

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








# def staffupdate(request, pk):
#     if request.method == 'GET':
#         staffform = StaffForm(instance=Staff.objects.get(pk=pk))
#     elif request.method == 'POST':
#         staffform = StaffForm(request.POST or None, instance=Staff.objects.get(pk=pk))
#         if staffform.is_valid():
#             obj= staffform.save(commit= False)
#             obj.image = request.FILES['image']
#             obj.save()      
#             return redirect('staff:staff_update', pk=pk)
#     return render(request, 'staff_add.html', {
#         'form': staffform,
#         })

class StaffDelete(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff:staff')

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)

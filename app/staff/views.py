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
            'first_name', 
            'last_name', 
            'is_staff', 
            'is_active', 
            'date_joined',
        ]
        context['metas'] = self.model._meta.fields
        context['form'] = StaffForm(self.request.POST)
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list('id', 'username', 'email', 'cell', 'image')

class StaffCreate(SuccessMessageMixin, CreateView):
    form_class = StaffForm
    template_name = 'staff_add.html'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return HttpResponseRedirect(reverse('staff:staff_update', kwargs={'pk': user.pk}))

def staffupdate(request, pk):
    if request.method == 'GET':
        staffform = StaffForm(instance=Staff.objects.get(pk=pk))
    elif request.method == 'POST':
        staffform = StaffForm(request.POST or None, instance=Staff.objects.get(pk=pk))

        if staffform.is_valid():
            obj= staffform.save(commit= False)
            obj.save()      
            return redirect('staff:staff_update', pk=pk)
    return render(request, 'staff_add.html', {
        'form': staffform,
        })

class StaffDelete(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff:staff')

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)

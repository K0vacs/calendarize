from django.shortcuts import render
from .models import Equipment
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import EquipmentForm

from django.forms.models import model_to_dict
from django.core import serializers
import json

class EquipmentTable(ListView):
    model = Equipment
    template_name = 'equipment.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        context['metas'] = self.model._meta.fields
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list()

class EquipmentCreate(SuccessMessageMixin, CreateView):
    form_class = EquipmentForm
    fields = '__all__'
    template_name = 'equipment_add.html'
    success_message = "%(name)s was created successfully"

    def get_success_url(self):
        return reverse_lazy('equipment:equipment_update', kwargs = { 'pk': self.object.id })

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        return context

class EquipmentUpdate(SuccessMessageMixin, UpdateView):
    form_class = EquipmentForm
    template_name = 'equipment_add.html'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = Equipment.objects.filter(pk=self.kwargs['pk'])
        context['test'] = test
        return context

    def get_queryset(self):
        query = Equipment.objects.filter(pk=self.kwargs['pk'])
        return query

class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment:equipment')

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
from .models import Equipment
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import EquipmentForm

# This class reads from the Equipment database records and displays the returned data in a table.
class EquipmentTable(ListView):
    model = Equipment
    template_name = 'equipment.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Equipment"
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list('id','name', 'price')

# This class creates new BD record(s) when the form is submitted
class EquipmentCreate(SuccessMessageMixin, CreateView):
    form_class = EquipmentForm
    template_name = 'equipment_add.html'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "New"
        context['title'] = "Equipment"
        context['form'] = self.form_class()
        return context

    def get_success_url(self):
        return reverse_lazy('equipment:equipment_update', kwargs = { 'pk': self.object.id })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

# This class updates existing BD record(s) when the form is submitted
class EquipmentUpdate(SuccessMessageMixin, UpdateView):
    form_class = EquipmentForm
    template_name = 'equipment_add.html'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Update"
        context['title'] = "Equipment"
        return context

    def get_queryset(self):
        query = Equipment.objects.filter(pk=self.kwargs['pk'])
        return query

# Delete individual DB record(s) in a modal
class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment:equipment')

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
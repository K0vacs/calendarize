from .models import Services
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ServiceTable(ListView):
    model = Services
    template_name = 'services.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Services"
        context['metas'] = self.model._meta.fields
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list()

class ServiceCreate(SuccessMessageMixin, CreateView):
    model = Services
    fields = '__all__'
    template_name = 'services_add.html'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "New"
        context['title'] = "Services"
        return context

class ServiceUpdate(SuccessMessageMixin, UpdateView):
    model = Services
    fields = '__all__'
    template_name = 'services_add.html'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Update"
        context['title'] = "Services"
        return context

class ServiceDelete(DeleteView):
    model = Services
    success_url = reverse_lazy('services:services')

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)

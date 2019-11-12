from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *

class ReadClass(ListView):
    template_name = 'customers.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        context['metas'] = self.model._meta.fields
        context['form'] = AuthorFormset(self.request.POST)
        return context

    def get_paginate_by(self, queryset):
        items_per_page = self.request.GET.get('results') or 10
        return items_per_page

    def get_queryset(self):
        return self.model.objects.all().values_list()

class CreateClass(SuccessMessageMixin, CreateView):
    # fields = '__all__'
    template_name = 'add.html'
    form_class = CustomersPriceForm
    success_message = "%(price)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        return context

class UpdateClass(SuccessMessageMixin, UpdateView):
    fields = '__all__'
    template_name = 'add.html'
    success_message = "%(price)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.object_name
        return context

class DeleteClass(DeleteView):
    success_url = reverse_lazy('customers')

    def get(self, request, **kwargs):
        return self.post(request, **kwargs)

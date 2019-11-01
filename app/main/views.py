from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from .models import Services
from .forms import ServicesForm
from django.urls import reverse_lazy
from main.utils import table


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def overview(request):
    return render(request, 'overview.html')

@login_required(login_url='/accounts/login/')
def services(request):
    context = table(request, Services)
    return render(request, 'pages/services.html', context)

# @login_required(login_url='/accounts/login/')
# def services_add_new(request):
#     form    = ServicesForm(request.POST)
#     results = Services.objects.get(pk=15)
#     if form.is_valid():
#         form.save()
#
#     context = { 'boo': form, 'results': results }
#     return render(request, 'pages/add-new.html', context)


class AddNew(CreateView):
    model = Services
    fields = '__all__'
    template_name = 'pages/add-new.html'

class Update(UpdateView):
    model = Services
    fields = '__all__'
    template_name = 'pages/add-new.html'

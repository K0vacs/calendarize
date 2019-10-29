from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Services, ServicesForm


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def overview(request):
    return render(request, 'overview.html')

@login_required(login_url='/accounts/login/')
def services(request):
    test = Services.objects.values_list(named=True)
    metas = Services._meta.fields
    results = Services.objects.all()[:15]
    context = { 'metas': metas, 'results': results, 'test': test }
    return render(request, 'pages/services.html', context)

@login_required(login_url='/accounts/login/')
def services_add_new(request):
    form = ServicesForm(request.POST)

    if form.is_valid():
        form.save()

    context = {'boo': form }
    return render(request, 'pages/add-new.html', context)

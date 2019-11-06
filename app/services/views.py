from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Services
from .utils import ReadClass, CreateClass, UpdateClass, DeleteClass


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def overview(request):
    return render(request, 'overview.html')

# CRUD on Services
class ServicesRead(ReadClass):
    model = Services

class ServicesCreate(CreateClass):
    model = Services

class ServicesUpdate(UpdateClass):
    model = Services

class ServicesDelete(DeleteClass):
    model = Services

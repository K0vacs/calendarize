from django.db import models
from django.urls import reverse
from customers.models import *
from services.models import *
from equipment.models import *
from staff.models import *
from django.utils import timezone

class Bookings(models.Model):
    date            = models.CharField(max_length=100, default=None, null=False)
    start_time       = models.CharField(max_length=100, default=None, null=True)
    end_time         = models.CharField(max_length=100, default=None, null=True)
    field           = models.CharField(max_length=100, default=None, null=True) 
    service         = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)
    equipment       = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
    staff           = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('bookings:bookings_update', kwargs={'pk': self.pk})

class CustomerStatus(models.Model):
    booking  = models.ForeignKey(Bookings, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True)
    status   = models.CharField(max_length=3)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('bookings:bookings_update', kwargs={'pk': self.pk})
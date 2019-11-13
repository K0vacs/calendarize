from django.db import models
from django.urls import reverse
from services.models import *

class Customers(models.Model):
    name    = models.CharField(max_length=100, default=None)
    email   = models.EmailField(max_length=100, default=None)
    cell    = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customers:customer_update', kwargs={'pk': self.pk})

class CustomersPrice(models.Model):
    services    = models.ForeignKey(Services, on_delete=models.CASCADE)
    price       = models.IntegerField(default=None)
    customer_id = models.IntegerField(default=None)

    def __str__(self):
        return self.price

    def get_absolute_url(self):
        return reverse('customers:customer_update', kwargs={'pk': self.pk})

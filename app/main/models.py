from django.db import models
from django.urls import reverse

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Services(models.Model):
    name        = models.CharField(max_length=100)
    capacity    = models.IntegerField()
    price       = models.IntegerField()

    def get_absolute_url(self):
        return reverse('update', kwargs= {
                                    'model': 'service',
                                    'pk': self.pk
                                 })

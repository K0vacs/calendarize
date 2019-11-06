from django.db import models
from django.urls import reverse

class Services(models.Model):
    name        = models.CharField(max_length=100)
    capacity    = models.IntegerField()
    price       = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services_update', kwargs={'pk': self.pk})

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Staff(AbstractUser):
    email   = models.EmailField(max_length=100)
    cell    = models.CharField(max_length=30)
    image   = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('staff:staff_update', kwargs={'pk': self.pk})
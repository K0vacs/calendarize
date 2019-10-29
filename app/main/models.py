from django.db import models
from django.forms import ModelForm

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

class Services(models.Model):
    name        = models.CharField(max_length=100)
    capacity    = models.IntegerField()
    price       = models.IntegerField()

    def __str__(self):
        return self.name

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'capacity', 'price']

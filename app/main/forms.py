from .models import Services, Person
from django.forms import ModelForm

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'capacity', 'price']

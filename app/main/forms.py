from .models import Services
from django.forms import ModelForm

class ServicesForm(ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'capacity', 'price']

class PersonForm(ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'capacity', 'price']

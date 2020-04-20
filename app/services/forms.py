from .models import Customers
from django.forms import ModelForm

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'cell', 'apples']

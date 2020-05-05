from .models import Customers
from django.forms import ModelForm

# Adding a static customer form
class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'cell', 'apples']

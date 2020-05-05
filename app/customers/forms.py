from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import Customers, CustomersPrice, Services

# Adding a static customers form
class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'cell']

# Adding a static customers price form
class CustomersPriceForm(forms.ModelForm):
    class Meta:
        model = CustomersPrice
        fields = ['services', 'price']

    services = forms.ModelChoiceField(queryset=Services.objects.all())
    price = forms.IntegerField()

# Modifying the customer price form to a dynamic formset
ServiceModelFormset = modelformset_factory(
    CustomersPrice, 
    form=CustomersPriceForm, 
    fields=('services', 'price'), 
    extra=1
)
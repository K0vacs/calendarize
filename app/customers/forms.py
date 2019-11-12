from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import *

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'cell']

class CustomersPriceForm(forms.ModelForm):
    class Meta:
        model = CustomersPrice
        fields = ['services', 'price']

    services = forms.ModelChoiceField(queryset=Services.objects.all())
    price = forms.IntegerField()

ServiceModelFormset = modelformset_factory(CustomersPrice, form=CustomersPriceForm, fields=('services', 'price'), extra=1,)

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'services']

    services = forms.ModelChoiceField(queryset=Services.objects.all())

BookModelFormset = modelformset_factory(Books, form=BookForm, fields=('name', 'services'), extra=1,)
















# BookModelFormset = modelformset_factory(
#     Books,
#     form=BookForm,
#     fields=('name', ),
#     extra=2,
#     widgets={'name': forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter Book Name here'
#         })
#     }
# )

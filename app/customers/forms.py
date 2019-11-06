from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import Services, Customers, CustomersPrice, Book

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

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'isbn_number']

BookModelFormset = modelformset_factory(Book, form=BookForm, fields=('name', 'isbn_number'), extra=2,)

# BookModelFormset = modelformset_factory(
#     Book,
#     form=BookForm,
#     fields=('name', ),
#     extra=2,
    # widgets={'name': forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter Book Name here'
    #     })
    # }
# )

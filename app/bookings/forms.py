from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory, inlineformset_factory
from .models import *
from .widgets import *
from services.models import *
from .validators import *

class BookingsDateForm(ModelForm):
    date = forms.CharField( 
        widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY', 'required': 'required'}),
        validators=[date_validation],
        label='',
        required=True
    )

    start_time = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'HH:MM', 'required': 'required', 'class': 'start-time'}),
        validators=[time_validation],
        label='',
        required=True
    )

    end_time = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'HH:MM', 'required': 'required'}),
        validators=[time_validation],
        label='',
        required=True
    )

    class Meta:
        model = Bookings
        fields = ('date', 'start_time', 'end_time')

class BookingsStaticForm(ModelForm):
    service = forms.ModelChoiceField(
        queryset=Services.objects.all(), 
        label='',
        required=True
    )
    equipment = forms.ModelChoiceField(
        queryset=Equipment.objects.all(), 
        label='',
        required=True
    )
    staff = forms.ModelChoiceField(
        queryset=Staff.objects.all(), 
        label='',
        required=True
    )

    class Meta:
        model = Bookings
        fields = ('service', 'equipment', 'staff')

class CustomerStatusForm(ModelForm):
    CHOICES = [
        ('1', 'Confirmed'),
        ('2', 'Cancelation'),
        ('3', 'Late Cancelation'),
    ]

    customer = forms.ModelChoiceField(
        queryset=Customers.objects.all(), 
        widget=forms.Select(attrs={
            'required': 'required',
            'placeholder': 'Customer',
        }),
        label='',
        required=True)

    status = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.Select(attrs={
            'required': 'required',
            'placeholder': 'Status',
        }),
        label='',
        required=True)

    class Meta:
        model = CustomerStatus
        fields = ('customer', 'status')

CustomerStatusModelFormset = modelformset_factory(
    CustomerStatus, 
    form=CustomerStatusForm, 
    fields=('customer', 'status'), 
    extra=1)

BookingsDateFormset = modelformset_factory(
    Bookings, 
    form=BookingsDateForm, 
    fields=('date', 'start_time', 'end_time'), 
    extra=1)
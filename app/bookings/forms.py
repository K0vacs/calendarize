from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import Bookings, Customers, Equipment, CustomerStatus, Staff
from services.models import Services
from .validators import date_validation, time_validation

class BookingsStaticForm(ModelForm):
    date = forms.CharField(
        required=True,
        widget=forms.DateInput(
            format="%d/%m/%Y",
            attrs={
            "id": "datetimepicker",
            "class": "form-control datetimepicker-input",
            "data-target": "#datetimepicker",
            "data-toggle": "datetimepicker",
            "pattern": "\d{1,2}/\d{1,2}/\d{4}",
            'placeholder': 'DD/MM/YYYY',
            "required": "true",
        })
    )

    start_time = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'HH:MM', 'required': 'required', 'class': 'start-time'}),
        validators=[time_validation],
        required=True
    )

    end_time = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'HH:MM', 'required': 'required'}),
        validators=[time_validation],
        required=True
    )

    equipment = forms.ModelChoiceField(
        queryset=Equipment.objects.all(), 
        required=True
    )

    service = forms.ModelChoiceField(
        queryset=Services.objects.all(), 
        required=True
    )

    staff = forms.ModelChoiceField(
        queryset=Staff.objects.all(), 
        required=True
    )

    class Meta:
        model = Bookings
        fields = ('date', 'start_time', 'end_time', 'equipment', 'service', 'staff')

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
        required=True)

    status = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.Select(attrs={
            'required': 'required',
            'placeholder': 'Status',
        }),
        required=True)

    class Meta:
        model = CustomerStatus
        fields = ('customer', 'status')

def customer_status_formset(number):
    CustomerStatusModelFormset = modelformset_factory(
        CustomerStatus, 
        form=CustomerStatusForm, 
        fields=('customer', 'status'), 
        extra=number
    )
    return CustomerStatusModelFormset
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import Bookings, Customers, Equipment, CustomerStatus, Staff
from services.models import Services
from .validators import date_validation, time_validation

class BookingsStaticForm(ModelForm):
    date = forms.CharField(
        label="",
        required=True,
        widget=forms.DateInput(
            format="%d/%m/%Y",
            attrs={
            "id": "datetimepicker",
            "class": "form-control datetimepicker-input",
            "data-target": "#datetimepicker",
            "data-toggle": "datetimepicker",
            "pattern": "\d{1,2}/\d{1,2}/\d{4}",
            "required": "true",
        })
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

    equipment = forms.ModelChoiceField(
        queryset=Equipment.objects.all(), 
        label='',
        required=True
    )

    service = forms.ModelChoiceField(
        queryset=Services.objects.all(), 
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

def customer_status_formset(number):
    CustomerStatusModelFormset = modelformset_factory(
        CustomerStatus, 
        form=CustomerStatusForm, 
        fields=('customer', 'status'), 
        extra=number
    )
    return CustomerStatusModelFormset

# def bookings_date_formset(number):
#     BookingsDateFormset = modelformset_factory(
#         Bookings, 
#         form=BookingsDateForm, 
#         fields=('date', 'start_time', 'end_time', 'equipment'), 
#         extra=number
#     )
#     return BookingsDateFormset
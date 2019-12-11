from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import *
from .widgets import *
from services.models import *
# from bootstrap_datepicker_plus import DatePickerInput


class BookingsDateForm(ModelForm):
    date = forms.CharField( 
        widget=DatePicker(),
        required=False
    )

    starttime = forms.CharField(
        widget=TimePicker(),
        required=False
    )

    endtime = forms.CharField(
        widget=TimePicker(),
        required=False
    )

    class Meta:
        model = Bookings
        fields = ('date', 'starttime', 'endtime')

class BookingsStaticForm(ModelForm):
    service     = forms.ModelChoiceField(queryset=Services.objects.all(), required=False)
    equipment   = forms.ModelChoiceField(queryset=Equipment.objects.all(), required=False)
    staff       = forms.ModelChoiceField(queryset=Staff.objects.all(), required=False)

    class Meta:
        model = Bookings
        fields = ('service', 'equipment', 'staff')

class CustomerStatusForm(ModelForm):
    CHOICES = [
        ('1', 'Confirmed'),
        ('2', 'Cancelation'),
        ('3', 'Late Cancelation'),
    ]

    customer    = forms.ModelChoiceField(queryset=Customers.objects.all())
    status      = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = CustomerStatus
        fields = '__all__'

CustomerStatusModelFormset = modelformset_factory(
    CustomerStatus, 
    form=CustomerStatusForm, 
    fields=('customer', 'status'), 
    extra=1)

BookingsDateFormset = modelformset_factory(
    Bookings, 
    form=BookingsDateForm, 
    fields=('date', 'starttime', 'endtime'), 
    extra=1)
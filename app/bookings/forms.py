from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from .models import *
from .widgets import *
from services.models import *
# from bootstrap_datepicker_plus import DatePickerInput


class BookingsForm(ModelForm):
    date = forms.DateField(
        input_formats=['%Y-%m-%d'], 
        widget=DatePicker(),
        required=False
    )

    starttime = forms.DateField(
        input_formats=['%H:%mm'], 
        widget=TimePicker(),
        required=False
    )

    endtime = forms.DateField(
        input_formats=['%H:%mm'], 
        widget=TimePicker(),
        required=False
    )
    # starttime = forms.DateField(
    #     widget=DatePickerInput(format='%m/%d/%Y'),
    #     required=False
    # )
    # endtime = forms.TimeField(
    #     input_formats=['%H:%M'], 
    #     widget=TimePicker(),
    #     required=False
    # )
    # date        = forms.CharField(required=False)
    service     = forms.ModelChoiceField(queryset=Services.objects.all(), required=False)
    equipment   = forms.ModelChoiceField(queryset=Equipment.objects.all(), required=False)
    staff       = forms.ModelChoiceField(queryset=Staff.objects.all(), required=False)

    class Meta:
        model = Bookings
        fields = '__all__'

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

# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )



# class DateForm(forms.Form):
#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'], 
#         widget=BootstrapDateTimePickerInput()
#     )
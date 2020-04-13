from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from bookings.validators import date_validation

class searchForm(forms.Form):

    search_date = forms.DateField(
        label="",
        input_formats=["%d/%m/%Y"],
        widget=forms.DateTimeInput(attrs={
            "id": "datetimepicker",
            "class": "form-control datetimepicker-input",
            "data-target": "#datetimepicker",
            "data-toggle": "datetimepicker",
            "pattern": "\d{1,2}/\d{1,2}/\d{4}",
            "required": "true",
        })
    )
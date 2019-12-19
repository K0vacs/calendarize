from django.core.exceptions import ValidationError
import datetime
from django import forms

def date_validation(value):
    try:
        date = datetime.datetime.strptime(value, '%d/%m/%Y')
    except:
        raise forms.ValidationError('DD/MM/YYYY format required')

def time_validation(value):
    try:
        time = datetime.datetime.strptime(value, '%H:%M')
    except:
        raise forms.ValidationError('HH:MM format required')

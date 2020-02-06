from django import forms
from django.forms import ModelForm
# from bookings.models import *
from bookings.validators import *

class searchForm(forms.Form):
    search_date = forms.CharField( 
        widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY', 'required': 'required'}),
        validators=[date_validation],
        label='',
        required=True
    )

#     class Meta:
#         model = Bookings
#         fields = ('search_date')
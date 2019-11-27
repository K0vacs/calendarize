from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class StaffForm(UserCreationForm):
    email   = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    cell    = forms.CharField(max_length=30)
    image   = forms.ImageField(label='', required=False)
    
    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'email', 'cell', 'image', 'password1', 'password2')

class StaffUpdateForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'email', 'cell', 'image', 'password')
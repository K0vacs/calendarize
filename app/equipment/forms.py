from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    icon = forms.ImageField(label='')
    class Meta:
        model = Equipment
        fields = ('name', 'icon', 'price')
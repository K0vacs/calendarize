from django import forms
from .models import Equipment

# Adding a static equipment form
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('name', 'price')
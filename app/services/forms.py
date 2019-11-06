from .models import Customers
from django.forms import ModelForm

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'cell', 'apples']

    # def save(self):
    #     for interest in self.cleaned_data[“interests”]:
    #         Customers.objects.create(
    #            profile=profile,
    #            interest=interest,
    #        )

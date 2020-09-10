from django import  forms
from .models import  PricingTable

class PricingForm(forms.ModelForm):
    class Meta:
        model=PricingTable
        fields="__all__"
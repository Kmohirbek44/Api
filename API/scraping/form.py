from django import forms
from .models import City,Language

class findForm(forms.Form):
    city=forms.ModelChoiceField(queryset=City.objects.all(),to_field_name='slug',required=False,
                                    widget=forms.Select(attrs={'class':'form-select'}))
    language = forms.ModelChoiceField(queryset=Language.objects.all(),to_field_name='slug',required=False,
                                      widget=forms.Select(attrs={'class':'form-select'}))

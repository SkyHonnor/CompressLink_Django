from django import forms

from .models import *

class RedirectionTableForm(forms.ModelForm):
    class Meta:
        model = RedirectionTable
        fields = ['urlredirection']
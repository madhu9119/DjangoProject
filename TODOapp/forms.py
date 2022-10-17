from dataclasses import fields
from django import forms
from .models import *

class Empform(forms.ModelForm):
    class Meta :
        model = EmpdataModel
        fields = "__all__"

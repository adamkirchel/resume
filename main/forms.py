from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import botModel
import pandas as pd

class botForm(forms.ModelForm):
    
    input = forms.CharField()
    
    class Meta:
        model = botModel
        fields = ("input",)
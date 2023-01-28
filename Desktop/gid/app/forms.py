from django import forms
from .models import *
from django.forms import ModelForm 

class Medical_History(ModelForm):
    class Meta:
        model = Application
        fields = ['medical_history']
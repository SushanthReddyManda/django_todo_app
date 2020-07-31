from django import forms

from django.forms import ModelForm

from .models import *

class model_class_form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Add new task..."}))
    class Meta:
        model = model_class
        fields= '__all__'

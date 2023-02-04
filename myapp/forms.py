from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class ContactForm(forms.ModelForm):
 
  class Meta:
    model = Contact
    fields = '__all__'
    widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Your Name','class':'form-control m-2 mb-3 pb-2'}),
            'email' : forms.TextInput(attrs={'placeholder':'Your Email','class':'form-control m-2 mb-3 pb-2'}),
            'message' : forms.TextInput(attrs={'placeholder':'Your message here...','class':'form-control', 'type':'text'}),
            

        }
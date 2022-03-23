from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
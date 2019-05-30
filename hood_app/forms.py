from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['business_owner']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user']
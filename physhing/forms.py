from django import forms
from .models import user
from django.core import validators

class insta(forms.ModelForm):
    class Meta:
        model=user
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
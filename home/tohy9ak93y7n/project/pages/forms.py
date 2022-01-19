from django import forms
from .models import Login
class Login_form(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']

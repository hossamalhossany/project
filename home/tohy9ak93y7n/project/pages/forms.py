from django import forms


class Login_form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

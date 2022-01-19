from django import forms
class Login_form(forms.Form):
    username = forms.CharField(max_length=50, label='name', initial='enter username')
    password = forms.CharField(max_length=50, label='password', initial='enter password', widget=forms.PasswordInput)

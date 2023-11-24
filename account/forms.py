from django import forms


class LoginForm(forms.Form):
    """
    Form for login in the app
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

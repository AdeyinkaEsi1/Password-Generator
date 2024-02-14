from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Password_gen_form(forms.Form):
    length = forms.IntegerField(min_value=5, max_value=20, initial=8, label='Password length')
    

class LoginForm(LoginView):
    
    class Meta:
        model = User
        fields = ['username', 'password',]


class UserRegForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.users.models import User


class LoginForm(forms.Form):
    '''Представляет собой форму для логина да
    '''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':"Username"
            }),
            label="Login",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password'
            }
        ),
        label="Password"
    )
    class Meta:
        model = User
        fields = ['email', 'password']


class PasswordChangeForm(forms.Form):
    '''Представляет собой форму смены
    пароля в личном кабинете
    '''
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'name':"old_password",
                'placeholder':'Старый пароль'
            }
        ),
        label="Старый пароль"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'name':"password",
                'placeholder':'Пароль'
            }
        ),
        label="Новый пароль"
    )
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'name':"password_repeat",
                'placeholder':'Повторите новый пароль'
            }
        ),
        label="Повторите новый пароль"
    )
    class Meta:
        model = User
        fields = ['password']

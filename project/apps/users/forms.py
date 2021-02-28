from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.users.models import User


class LoginForm(forms.Form):
    '''Представляет собой форму для логина да
    '''
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'type':'email',
                'name':'email',
                'placeholder':"Email"
            }),
            label="Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'name':"password",
                'placeholder':'password'
            }
        ),
        label="Password"
    )
    class Meta:
        model = User
        fields = ['email', 'password']


class PasswordResetForm(forms.Form):
    '''Представляет собой форму смены
    пароля в личном кабинете
    '''
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'name':"old_password",
                'placeholder':'old_password'
            }
        ),
        label="Password"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'name':"password",
                'placeholder':'password'
            }
        ),
        label="Password"
    )
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'name':"password_repeat",
                'placeholder':'repeat your password'
            }
        ),
        label="Password"
    )
    class Meta:
        model = User
        fields = ['password']


class PasswordChangeForm(forms.Form):
    '''Представляет собой форму ресета пароля
    '''
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'name':"password",
                'placeholder':'password'
            }
        ),
        label="Password"
    )
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'name':"password_repeat",
                'placeholder':'repeat your password'
            }
        ),
        label="Password"
    )

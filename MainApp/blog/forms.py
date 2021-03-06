from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth.models import User


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

#Форма для регистрации
class RegisterUserForm(UserCreationForm):
    class Meta:
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        model = User
        fields = ('username', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        # }


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    age = forms.IntegerField(max_value=999, label='Введите возраст')

    class Meta:
        model = User
        fields = ['username', 'age', 'password1', 'password2']
        labels = {
            'username': 'Введите логин',
            'password1': 'Введите пароль',
            'password2': 'Повторите пароль',
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 30:
            raise forms.ValidationError('Логин должен быть не длиннее 30 символов.')
        return username

from django.contrib.auth.models import User
from django import forms
from app.models import Table_com

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class Table_comForm(forms.ModelForm):
    class Meta:
        model = Table_com
        fields = ['text']  # поля которые нужно отобразить кроме тех что заполняются автоматически
        # можно явноуказывать список полей ['name', 'price']

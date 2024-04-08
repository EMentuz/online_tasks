from django import forms
from app.models import Task


class MyForm(forms.ModelForm):
    class Meta:
        model = Task # связываем форму с моделью Product
        fields = '__all__' # поля которые нужно отобразить кроме тех что заполняются автоматически
        # можно явноуказывать список полей ['name', 'price']

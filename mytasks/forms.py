from django import forms
from app.models import Task


class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']
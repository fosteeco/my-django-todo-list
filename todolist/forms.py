from django import forms
from .models import todoItem

class todoForm(forms.ModelForm):
    class Meta:
        model = todoItem
        fields = ['description', 'priority']
        labels = {'description': 'Description', 'priority': 'Priority'}



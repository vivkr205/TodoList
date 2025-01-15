from django import forms
from TodoApp.models import Tasklist

class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasklist
        fields=['task','done']
    

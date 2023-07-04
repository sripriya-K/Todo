from django import forms
from todoapp.models import Notes
class MyForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','description')
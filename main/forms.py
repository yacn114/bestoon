from django import forms
from .models import Expensive,Income

class ExpensiveForm(forms.ModelForm):
    class Meta:
        model = Expensive
        fields = ['title', 'amount', 'date','user']
        widgets = {
            'title': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['title', 'amount', 'date']
        widgets = {
            'title': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

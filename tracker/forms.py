from django import forms
from .models import Expense, Income


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'date', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['category', 'date', 'amount', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
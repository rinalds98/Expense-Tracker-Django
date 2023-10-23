from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from .forms import ExpenseForm, IncomeForm

def index(request):
    return render(request, 'index.html')

@login_required
def budget(request):
    expenses = Expense.objects.filter(user=request.user)
    income = Income.objects.filter(user=request.user)
    total_income = 0
    total_expenses = 0
    for money in income:
        total_income += money.amount
    for money in expenses:
        total_expenses += money.amount
    user= request.user.username
    context = {
        'total_expenses': total_expenses,
        'total_income': total_income,
        'user': user,
    }
    return render(request, 'budget.html', context)

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('budget')
    else:
        form = ExpenseForm()
    context = {
        'form': form,
    }
    return render(request, 'add_expense.html', context)


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('budget')
    else:
        form = IncomeForm()
    context = {
        'form': form,
    }
    return render(request, 'add_income.html', context)
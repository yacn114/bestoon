from django.shortcuts import render,redirect
from .models import Expensive,Income
from django.db.models import Sum
from .forms import ExpensiveForm,IncomeForm
def main(request):
    income = Income.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
    expenses = Expensive.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
    transactions = expenses + income
    balance = income - expenses

    context = {
        'transactions': transactions,
        'income': income,
        'expenses': expenses,
        'balance': balance,
    }
    return render(request, 'main.html', context)

def add_transaction(request):
    form1 = ExpensiveForm()
    form2 = IncomeForm()

    if request.method == 'POST':
        if 'submit_form1' in request.POST:
            form1 = ExpensiveForm(request.POST)
            if form1.is_valid():
                form1.user = request.user
                form1.save()
                return redirect('main')
        elif 'submit_form2' in request.POST:
            form2 = IncomeForm(request.POST)
            if form2.is_valid():
                form2.user = request.user
                form2.save()
                return redirect('main')
    else:
        form2 = IncomeForm()
        form1 = ExpensiveForm()
    
    return render(request, 'add_transaction.html', {'form1': form1,'form2': form2,})

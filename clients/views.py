from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Savings, Transfer, Transaction
from .forms import TransferForm
from django.contrib import messages

# Create your views here.

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    account = get_object_or_404(Savings, user=user)
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            amount = form.cleaned_data['amount']
            transfer_pin = account.pin
            description = form.cleaned_data['description']
            if not int(pin) == int(transfer_pin):
                messages.error(request, "wrong pin entered.")
            elif (account.balance - 150) <= amount:
                    messages.warning(request, "balance too low, Balance shouldnt be less than $150 after transfer.")
            else:
                obj, created = Transfer.objects.get_or_create(
                    user = user,
                    account = account,
                    amount= amount,
                    swift_code= form.cleaned_data['swift_code'],
                    receivers_name= form.cleaned_data['receivers_name'],
                    beneficiary_account_number= form.cleaned_data['beneficiary_account_number'],
                    beneficiary_bank_address= form.cleaned_data['beneficiary_bank_address'],
                    description = description,
                    country= form.cleaned_data['country']
                )

                Transaction.objects.create(
                    user=user, 
                    record='debit', 
                    amount=amount, 
                    description=description,
                    is_success="pending"
                )
                
                messages.success(request,'Transfer Has Been Submitted. Transfer is Under Processing.')
                return redirect("clientprofile", user.username)
    else:
        form = TransferForm()
    
    context = {
        "user": user,
        "form": form,
        "account": account,
    }
    return render(request, 'users/profile.html', context)


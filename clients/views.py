from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import (
    CustomUser, Savings, Transfer, 
    Transaction, CardRequest
)
from .forms import TransferForm, CardRequestForm
from django.contrib import messages

# Create your views here.

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    account = get_object_or_404(Savings, user=user)
    short_transactions = Transaction.objects.all().order_by('-transaction_date')[:5]
    total_transfer = Transfer.objects.count()
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
                if created:
                    Transaction.objects.create(
                        user=user, 
                        record='debit', 
                        amount=amount, 
                        description=description,
                        status="pending",
                        reference= obj.reference
                    )
                    
                    messages.success(request,'Transfer Has Been Submitted. Transfer is Under Processing.')
                    return redirect("clientprofile", user.username)
    else:
        form = TransferForm()
    
    context = {
        "user": user,
        "form": form,
        "account": account,
        's_transactions': short_transactions,
        "total_transfers": total_transfer
    }
    return render(request, 'users/profile.html', context)


@login_required
def current_user_profile(request):
    if request.user.is_staff:
        return redirect('admindashboard')
    return redirect('clientprofile', username=request.user.username)


@login_required
def card_request(request):
    
    if request.method == "POST":
        form = CardRequestForm(request.POST)
        if form.is_valid():
            cardtype = form.cleaned_data['cardtype']
            CardRequest.objects.create(cardtype=cardtype, user=request.user)
            messages.success(request,'Request is being processed, Our bank will contact.')
            return redirect("clientprofile", request.user.username)
    else:
        form = CardRequestForm()
    context = {
        "form": form,
        "title": "card request"
    }
    return render(request, 'users/cardrequest.html', context)


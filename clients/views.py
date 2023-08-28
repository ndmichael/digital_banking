from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Savings
from .forms import TransferForm

# Create your views here.

@login_required
def profile(request, username):
    form = TransferForm()
    user = get_object_or_404(CustomUser, username=username)
    account = get_object_or_404(Savings, user=user)
    context = {
        "user": user,
        "form": form,
        "account": account,
    }
    return render(request, 'users/profile.html', context)


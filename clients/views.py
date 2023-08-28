from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import TransferForm

# Create your views here.

@login_required
def profile(request, username):
    form = TransferForm()
    user = get_object_or_404(CustomUser, username=username)
    context = {
        "user": user,
        "form": form
    }
    return render(request, 'users/profile.html', context)


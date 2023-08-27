from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.

@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context = {
        "user": user
    }
    return render(request, 'users/profile.html', context)


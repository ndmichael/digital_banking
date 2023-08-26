from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')


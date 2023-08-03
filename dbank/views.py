from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'dbank/index.html', {'title': 'home'})


def about(request):
    return render(request, 'dbank/about.html', {'title': 'about'})
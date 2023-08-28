from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("clientprofile", username=request.user.username)
    return render(request, 'dbank/index.html', {'title': 'home'})


def about(request):
    return render(request, 'dbank/about.html', {'title': 'about'})

def investments(request):
    return render(request, 'dbank/investments.html', {'title': 'investments'})

def visagold(request):
    return render(request, 'dbank/visagold.html', {'title': 'visa gold'})

def visainfinite(request):
    return render(request, 'dbank/visainfinite.html', {'title': 'visa infinite'})

def visaplatinum(request):
    return render(request, 'dbank/visaplatinum.html', {'title': 'visa platinum'})

def bank_account_types(request):
    return render(request, 'dbank/accounttypes.html', {'title': 'visa infinite'})
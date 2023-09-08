from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyCustomSignupForm, ClientUpdateForm, DeactivateUser, LoadBalanceForm
from clients.models import  CustomUser, Transfer, Savings
from random import randrange
from django.contrib import messages

# Create your views here.


def admin_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'title': 'admin-dashboard'})


def register(request):
    # if not request.user.is_staff:
    #     messages.error(
    #             request, f"You do not have permission to access this page."
    #         )
        # return redirect("/")
    if request.method == "POST":
        c_form = MyCustomSignupForm(request.POST,  request.FILES)
        if c_form.is_valid():
            balance = c_form.cleaned_data.get("balance")
            username = c_form.cleaned_data.get("username")
            country = c_form.cleaned_data.get("country")
            
            user = c_form.save(request)
               
            print(f"country: {country} balance: {balance}")
            number = [randrange(10) for i in range(10)]
            number = ''.join(str(i) for i in number)
            pin = number[:4]

            Savings.objects.create(user=user, number=number, balance=balance, pin=pin)

            # EMAILING 
            '''subject = f"Account Creation"
            message = f"""'success', Account has been created for {username}.
                password:....
            """
            sender = "mickeyjayblest@gmail.com"
            send_mail(
                subject,
                message,
                'mickeyjayblest@gmail.com',
                ['ukejemicheal@gmail.com']
            )'''

            messages.success(
                request, f"Account has been created for {username} you  can now login."
            )
            return redirect("all_users")
    else:
        c_form = MyCustomSignupForm()
    context = {
        'c_form': c_form,
        'title': "Registeration"
    }
    return render(request, 'dashboard/register.html', context)


def all_users(request):
    users = CustomUser.objects.filter(is_active=True, is_staff=False)
    total_clients = CustomUser.objects.count()
    deactivate_form = DeactivateUser()
    if request.POST:
        username = request.POST.get('username')
        print("username: ", username)
        if  request.POST.get('deactivate') == 'on':
            user = get_object_or_404(CustomUser, username=username)
            
            user.is_active = False
            user.save()
            messages.success(
                request, f"{username} has been deactivated."
            )
            return redirect(
                    "all_users"
                ) 
    context = {
        'users': users,
        'd_form': deactivate_form,
        'total_clients': total_clients
    }
    return render(request, 'dashboard/all_users.html', context)

def all_transfers(request):
    transfers = Transfer.objects.all()
    context = {
        'transfers': transfers,
    }
    return render(request, 'dashboard/all_transfers.html', context)

def update_user(request, username):
    user = get_object_or_404(
            CustomUser, username=username
        )
    if request.method == "POST":
        form = ClientUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f"account successfully updated")
            return redirect(
                "all_users"
            )  
    else:
        form = ClientUpdateForm(instance=user)
    context ={
        'form': form,
    }
    return render(request, 'dashboard/update_user.html', context)


def load_balance(request, username):
    client = get_object_or_404(CustomUser, username=username)
    savings = get_object_or_404(Savings, user=client)
    if request.POST:
        form = LoadBalanceForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get("amount")
            savings.balance += amount
            savings.save()
            messages.success(
                request, f"{client.username} current balance is {savings.balance}."
            )
            return redirect(
                "all_users"
            ) 
    else:
        form = LoadBalanceForm()
    context = {
        'client': client,
        'form': form
    }
    return render(request, 'dashboard/load_balance.html', context)
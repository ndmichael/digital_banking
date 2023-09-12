from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyCustomSignupForm, ClientUpdateForm, DeactivateUser, LoadBalanceForm, TransferStatusForm
from clients.models import  CustomUser, Transfer, Savings, Transaction
from random import randrange
from django.contrib import messages
from decimal import Decimal

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
    users = CustomUser.objects.filter(is_active=True, is_staff=False).order_by('-date_joined')
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
    transfers = Transfer.objects.all().order_by('-dotf')
    form = TransferStatusForm()
    if request.method == "POST":
        status = request.POST.get('status')
        transfer_id = request.POST.get('id')
                
        transfer = get_object_or_404(Transfer, id=transfer_id)
        user = CustomUser.objects.get(id=transfer.user.id)
        bank_acc = Savings.objects.get(user=user)
        transaction = Transaction.objects.get(user=user, reference=transfer.reference)

        if status == "success":
            charges = transfer.amount * Decimal(0.02)
            if transaction.record == 'credit':
                transaction.amt_aft_charges = transaction.amount - charges
            else:
                transaction.amt_aft_charges = transaction.amount + charges
            
            bank_acc.balance = bank_acc.balance - transaction.amt_aft_charges
            bank_acc.save()

        transaction.status = status
        transfer.status = status
        transaction.save()
        transfer.save()
    
    context = {
        'transfers': transfers,
        "form": form
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


def historypage(request):
    context = {

    }
    return render(request, 'dashboard/historypage.html', context)
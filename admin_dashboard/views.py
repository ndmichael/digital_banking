from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyCustomSignupForm, ClientUpdateForm
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
    users = CustomUser.objects.all()
    context = {
        'users': users,
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
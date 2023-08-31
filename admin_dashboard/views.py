from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyCustomSignupForm
from clients.models import  CustomUser, Transfer

# Create your views here.


def admin_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'title': 'admin-dashboard'})


def register(request):
    # if not request.user.is_staff:
    #     messages.error(
    #             request, f"You do not have permission to access this page."
    #         )
    #     return redirect("/")
    # if request.method == "POST":
    #     u_form = UserForm(request.POST)
    #     c_form = ClientRegisterForm(request.POST,  request.FILES)
    #     if u_form.is_valid() and c_form.is_valid():
    #         user = u_form.save()
    #         client = c_form.save(commit=False)
    #         number = [randrange(10) for i in range(10)]
    #         acc_number = ''.join(str(i) for i in number)
    #         pin = acc_number[:4]
    #         client.user = user
    #         client.transfer_pin = pin
    #         client.account_number = acc_number
    #         client.save()
    #         username = u_form.cleaned_data.get("username")

    #         # EMAILING 
    #         '''subject = f"Account Creation"
    #         message = f"""'success', Account has been created for {username}.
    #             password:....
    #         """
    #         sender = "mickeyjayblest@gmail.com"
    #         send_mail(
    #             subject,
    #             message,
    #             'mickeyjayblest@gmail.com',
    #             ['ukejemicheal@gmail.com']
    #         )'''

    #         messages.success(
    #             request, f"Account has been created for {username} you  can now login."
    #         )
    #         return redirect("all_users")
    # else:
    #     u_form = UserForm()
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
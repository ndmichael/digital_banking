from django.shortcuts import render

# Create your views here.


def admin_dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'title': 'admin-dashboard'})
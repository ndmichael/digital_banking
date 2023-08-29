from django.shortcuts import render

# Create your views here.


def admin_dashboard(request):
    return render(request, 'dashboard/admin.html', {'title': 'admin-dashboard'})
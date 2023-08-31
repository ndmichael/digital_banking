from django.urls import path
from .views import (
    admin_dashboard,
    register,
    all_users,
    all_transfers
)



urlpatterns = [
    path("", admin_dashboard, name="admindashboard"),
    path("register/", register, name="register"),
    path("users/all/", all_users, name="all_users"),
    path("transfer/all/", all_transfers, name="all_transfers"),
]
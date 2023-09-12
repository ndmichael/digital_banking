from django.urls import path
from .views import (
    admin_dashboard,
    register,
    all_users,
    all_transfers,
    update_user,
    load_balance,
    historypage,
    addtransaction,
)



urlpatterns = [
    path("", admin_dashboard, name="admindashboard"),
    path("register/", register, name="register"),
    path("users/all/", all_users, name="all_users"),
    path("transfer/all/", all_transfers, name="all_transfers"),
    path("user/history/", historypage, name="historypage"),
    path("user/history/add/<str:username>/", addtransaction, name="addtransaction"),
    path("update/user/<str:username>/", update_user, name="update_user"),
    path("loadbalance/<str:username>/", load_balance, name="loadbalance"),
]
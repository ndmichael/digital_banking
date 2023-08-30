from django.urls import path
from .views import (
    admin_dashboard,
    register
)



urlpatterns = [
    path("", admin_dashboard, name="admindashboard"),
    path("register/client/", register, name="register"),
]
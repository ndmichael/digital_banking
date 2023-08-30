from django.urls import path
from .views import (
    admin_dashboard
)



urlpatterns = [
    path("", admin_dashboard, name="admindashboard"),
]
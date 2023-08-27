from django.urls import path
from .views import profile




urlpatterns = [
    path('profile/<str:username>', profile , name="clientprofile"),
]
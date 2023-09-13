from django.urls import path
from .views import profile, current_user_profile




urlpatterns = [
    path('profile/<str:username>', profile , name="clientprofile"),
    path('', current_user_profile, name="currentprofile")
]
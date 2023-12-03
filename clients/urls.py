from django.urls import path
from .views import (
    profile, current_user_profile, 
    card_request
)




urlpatterns = [
    path('profile/<str:username>', profile , name="clientprofile"),
    path('', current_user_profile, name="currentprofile"),
    path('user/cards/request', card_request, name="card_request"),
]
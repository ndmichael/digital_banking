from django.urls import path
from .views import index, about, investments




urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('investments/', investments, name="investments"),
]
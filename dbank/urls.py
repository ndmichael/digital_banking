from django.urls import path
from .views import index, about, investments, visagold




urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('investments/', investments, name="investments"),
    path('virtualcards/visagold', visagold, name="vcard"),
    path('virtualcards/visainfinite', visagold, name="vcard"),
]
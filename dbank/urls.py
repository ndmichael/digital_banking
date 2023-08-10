from django.urls import path
from .views import index, about, investments, visagold, visainfinite, bank_account_types




urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('investments/', investments, name="investments"),
    path('virtualcards/visagold', visagold, name="visagold"),
    path('virtualcards/visainfinite', visainfinite, name="visaInfinite"),
    path('virtualcards/visaplatinum', visainfinite, name="visaInfinite"),
    path('banking/accounts/types', bank_account_types, name="baccounts"),
]
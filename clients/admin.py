from django.contrib import admin
from .models import Savings, CustomUser, FixedDeposit, Card

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Savings)
admin.site.register(FixedDeposit)
admin.site.register(Card)
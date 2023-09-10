from django.contrib import admin
from .models import Savings, CustomUser, FixedDeposit, Card, Transfer, Transaction
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# admin.site.register(CustomUser)
admin.site.register(Savings)
admin.site.register(FixedDeposit)
admin.site.register(Card)
admin.site.register(Transfer)
admin.site.register(Transaction)

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_filter = ["is_staff"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password", "is_staff", "is_active"]}),
        (
            "Other info",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "gender",
                    "dob",
                    "country",
                    "address",
                ],
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "fields": [
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "country",
                    "address"
                ]
            },
        ),
    ]

# admin.site.register(CustomUser, UserAdmin)
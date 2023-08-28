from django.contrib import admin
from .models import Savings, CustomUser, FixedDeposit, Card
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# admin.site.register(CustomUser)
admin.site.register(Savings)
admin.site.register(FixedDeposit)
admin.site.register(Card)

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_filter = ["is_staff"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Other info",
            {
                "fields": [
                    "first_name",
                    "last_name",
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
                ]
            },
        ),
    ]

# admin.site.register(CustomUser, UserAdmin)
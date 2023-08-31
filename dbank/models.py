from django.db import models
from clients.models import CustomUser, Savings
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.




class Transfer(models.Model):
    status_choices = (
        ('success', 'SUCCESS'),
        ('pending', 'PENDING'),
        ('failed', 'FAILED')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cl_transfer")
    account = models.ForeignKey(Savings, on_delete=models.CASCADE, related_name="acc_transfer")
    currency = models.CharField(max_length=10, default="US DOLLAR")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    swift_code = models.CharField(max_length = 11, blank=True, null=True)
    receivers_name = models.CharField(max_length=50)
    beneficiary_account_number = models.CharField(max_length=20)
    beneficiary_bank_address = models.TextField()
    country = CountryField()
    dotf = models.DateTimeField(default=timezone.now)
    is_success =  models.CharField(choices=status_choices, default="pending")
    reference = models.CharField(null=False, blank=False, max_length=15)

    def __str__(self):
        return f'{self.receivers_name}'


class Transaction(models.Model):
    RECORD = (
        ('credit', 'CREDIT'),
        ('debit', 'DEBIT')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="history")
    record = models.CharField(default='credit', choices=RECORD, max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    amt_aft_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description =models.TextField(null=True, blank=True)
    transaction_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_date}"
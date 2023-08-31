from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, BaseUserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.postgres.fields import CICharField, CIEmailField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.mail import send_mail
# from dateutil.relativedelta import relativedelta




# Create your models here.

def today():
    return timezone.now().date

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    gender = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('non binary', 'NON BINARY')
    )
    username  = models.CharField(
        _("username"),
        max_length= 150,
        unique= True,
        help_text= _("Required. 150 characters or fewer. letters, digits, and @/./+/-/_ only"),
        validators= [username_validator],
        error_messages= {
            "unique": _("A user with the username already exists.")
        }
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(
        _("email address"),
        unique= True,
        error_messages= {
            "unique": _("A user with that email address already exists.")
        }                       
    )
    mobile_number = models.CharField(_("mobile number"), max_length=20, blank=True)
    address = models.TextField()
    country = CountryField()
    dob = models.DateField(default=timezone.now)
    gender= models.CharField(max_length=50, choices=gender, default="male")
    image = models.ImageField(default='avatar.png', upload_to='profile_pics/', blank=True, null=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text = _("Designates whether a user can login to admin site."),

    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text = _("Designates whether a user should be treated as active, deselect rather than to delete account."),

    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['-date_joined']
        abstract = False
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        self.username = self.username.lower()
        self.email = self.email.lower()
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Savings(models.Model):
    TIER_TUP = (
        ('tier1', 'TIER1'),
        ('tier2', 'TIER2'),
        ('tier3', 'TIER3')
    )
    user = models.OneToOneField(CustomUser, unique=True, on_delete=models.CASCADE, related_name="savings")
    number = models.CharField(max_length=20,  null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    tiers = models.CharField(max_length=10, choices=TIER_TUP, default="tier1")
    pin = models.CharField(max_length=4, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.number}"


class FixedDeposit(models.Model):
    interest_type = (
        ('monthly', 'MONTHLY'),
        ('yearly', 'YEARLY')
    )
    user = models.OneToOneField(CustomUser, unique=True, on_delete=models.CASCADE, related_name="fixeddeposit")
    number = models.CharField(max_length=20,  null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    pin = models.CharField(max_length=4, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    int_type = models.CharField(default='gold', choices=interest_type, max_length=10)
    duration = models.DateField(default=today)
    
    def interest(self):
        pass


class Investment(models.Model):
    pass


class Card(models.Model):
    cardTypes = (
        ('gold', 'GOLD'),
        ('infinite', 'INFINITE'),
        ('platinum', 'PLATINUM')
    )
    user = models.ForeignKey(CustomUser, unique=False, on_delete=models.CASCADE, related_name="client")
    cardtype = models.CharField(default='gold', choices=cardTypes, max_length=10)
    number = models.CharField(max_length=16,  null=True, blank=True)
    cvv = models.CharField(max_length=3,  null=True, blank=True)
    zipcode = models.CharField(max_length=7,  null=True, blank=True)
    status = models.BooleanField(default=True)
    address = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def ExpiringDate(self):
        expires = self.created - timezone.timedelta(days=1460)
        return expires


class Transfer(models.Model):
    status_choices = (
        ('success', 'SUCCESS'),
        ('pending', 'PENDING'),
        ('failed', 'FAILED')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bank_transfer")
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
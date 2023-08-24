from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, BaseUserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.postgres.fields import CICharField, CIEmailField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.mail import send_mail




# Create your models here.

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

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
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

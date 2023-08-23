from django.db import models
from django.contrib.auth.admin import User
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_countries.fields import CountryField




# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    gender = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('non binary', 'NON BINARY')
    )
    username  = CICharField(
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
    email = CIEmailField(
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
    gender= models.CharField(max_length=7, choices=gender, default="male")
    image = models.ImageField(default='avatar.png', upload_to='profile_pics/', blank=True, null=True)

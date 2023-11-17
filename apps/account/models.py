#!Python Modules
import os
import uuid


#!Django Function
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator


#!Third Party Packages
from PIL import Image
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField, RandomCharField
from django_countries.fields import CountryField


#!Helpers methods and functions
from config.helpers import setFullName


# ?MyAccountManager
class MyAccountManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superadmin", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self._create_user(email, password, **extra_fields)


# *Account
class Account(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        ADMIN = (
            "ADMIN",
            _("admin"),
        )
        SELLER = "SELLER", _("seller")
        BUYER = "BUYER", _("buyer")

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", _("active")
        INACTIVE = "INACTIVE", _("inactive")

    class Gender(models.TextChoices):
        MALE = "MALE", _("male")
        FEMALE = "FEMALE", _("female")

    email = models.EmailField(_("Email"), max_length=100, unique=True)
    first_name = models.CharField(
        _("First name"), max_length=150, blank=False, null=True
    )  # Add validation here
    last_name = models.CharField(
        _("Last name"), max_length=150, blank=False, null=True
    )  # Add validation here
    username = models.CharField(_("Username"), max_length=150, blank=True)
    phone = models.CharField(
        _("Phone"), max_length=100, blank=False, null=True, unique=True
    )  # Use vue js for phone validation
    photo = models.ImageField(
        _("Photo"),
        upload_to="account",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["png", "jpg", "jpeg"])],
    )
    is_admin = models.BooleanField(
        _("Admin status"),
        default=False,
        help_text=_("Designates whether the user is admin or not."),
    )
    is_staff = models.BooleanField(
        _("Staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    is_superadmin = models.BooleanField(
        _("Superadmin"),
        default=False,
        help_text=_("Designates whether the user is admin or not."),
    )
    date_joined = models.DateTimeField(_("Data joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("Last login"), auto_now_add=True)

    account_type = models.CharField(
        _("Account type"),
        max_length=20,
        choices=Types.choices,
        default=Types.choices[2][0],
        null=True,
        blank=False,
    )
    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=Status.choices,
        null=True,
        default=Status.choices[0][1],
    )
    gender = models.CharField(
        _("Gender"), max_length=20, choices=Gender.choices, null=True, blank=True
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone",
    ]  # this list in data macthes Account class one-by-one

    objects = MyAccountManager()

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        if not self.username:
            username = setFullName(self.first_name, self.last_name)
            ex = __class__.objects.filter(username=username).exists()
            while ex:
                i = len(
                    __class__.objects.filter(
                        first_name=self.first_name, last_name=self.last_name
                    )
                )
                username = f"{self.first_name} {self.last_name}{i+1}"
                ex = __class__.objects.filter(
                    username=username
                ).exists()  # If return false,break out while loop and save username to database
            self.username = username
        super(Account, self).save(*args, **kwargs)

    def get_username(self):
        return f"{self.username}"


# *Profile
class Profile(models.Model):
    account = models.OneToOneField(
        Account, verbose_name=(_("Account")), on_delete=models.CASCADE
    )
    slug = AutoSlugField(
        _("Slug"), populate_from="account", unique=True, db_index=True, blank=True
    )
    country = CountryField(verbose_name=_("Country"), blank=True)
    profile_key = RandomCharField(
        _("Profile Id"), length=24, unique=True, blank=True, include_alpha=True
    )
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    adress = models.CharField(_("Adress"), max_length=50, null=True, blank=True)
    additional_information = models.TextField(_("Additional Information"), blank=True)

    def __str__(self):
        return f"{self.account.username}"

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")


# create_user_profile
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(account=instance)


post_save.connect(create_user_profile, Account)

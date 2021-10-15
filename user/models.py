from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from user.manager import CustomAccountManager
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Name")
    email = models.EmailField(blank=False, null=True, unique=True, verbose_name="Email")
    is_staff = models.BooleanField(default=False, null=False, verbose_name="Is_staff")
    is_superuser = models.BooleanField(default=False, null=False, verbose_name="is_active")
    is_active = models.BooleanField(default=False, null=False, verbose_name="is_active")
    favourite_books = models.ManyToManyField(to="book.Book", blank=False, verbose_name="Favourite_books",
                                             related_name="Users")
    balance = models.DecimalField(blank=False, null=False, default=0, max_digits=7, decimal_places=2,
                                  verbose_name="Balance")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="Date_joined")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomAccountManager()

    def __str__(self):
        return self.email


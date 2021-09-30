from django.db import models
from book.models import Book
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Name")
    email = models.EmailField(blank=False, null=True, unique=True, verbose_name="Email")
    favourite_books = models.ManyToManyField(to=Book, blank=False, verbose_name="Favourite_books", related_name="Users")
    balance = models.DecimalField(blank=False, max_digits=7, decimal_places=2, verbose_name="Balance")

    USERNAME_FIELD="email"

    def __str__(self):
        return self.name

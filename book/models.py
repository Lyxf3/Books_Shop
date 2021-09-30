from django.db import models
from django.utils import timezone
import uuid


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name="Title")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="First_name")
    second_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Second_name")


class Publisher(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Title")

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name="Title")
    price = models.PositiveIntegerField(blank=False, verbose_name="Price")
    issued = models.DateTimeField(default=timezone.now, verbose_name="Issued")
    category = models.ForeignKey(to=Category, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Category")
    authors = models.ManyToManyField(to=Author, blank=False, null=True, verbose_name="Authors")
    market_id = models.PositiveIntegerField(blank=False, verbose_name="Publisher")
    discount_shop = models.PositiveSmallIntegerField(blank=False, verbose_name="Discount_shop")
    discount_market = models.PositiveSmallIntegerField(blank=False, verbose_name="Discount_market")
    available = models.BooleanField(default=False, verbose_name="Available")

    def __str__(self):
        return self.title


class PBook(Book):
    publisher = models.ForeignKey(to=Publisher, on_delete=models.SET_NULL, verbose_name="Publisher")


class EBook(Book):
    source = models.URLField(blank=True, null=True, verbose_name="Source")


class ABook(Book):
    file = models.FileField(upload_to=None, blank=True, null=True, verbose_name="File")


class BBook(Book):
    publisher = models.ForeignKey(to=Publisher,on_delete=models.SET_NULL,  blank=True, null=True, related_name="Book_for_blind",
                                  verbose_name="Publisher")


class PromoCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    percent = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Percent")
    user = models.ForeignKey(to="user.User", on_delete=models.CASCADE, verbose_name="User")
    times_to_use = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Times_to_use")
    times_used = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Times_used")

    def __str__(self):
        return self.id
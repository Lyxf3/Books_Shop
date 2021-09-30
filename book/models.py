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


class Contract(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name="author")
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, related_name="publisher")


class Market(models.Model): # TODO
    title = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name="Title")
    price = models.PositiveIntegerField(blank=False, verbose_name="Price")
    issued = models.DateTimeField(default=timezone.now, verbose_name="Issued")
    categories = models.ManyToManyField(to=Category, blank=False,
                                        related_name="books", verbose_name="Categories")
    authors = models.ManyToManyField(to=Author, blank=False, related_name="books",
                                     verbose_name="Authors")
    publisher = models.ForeignKey(to=Publisher, on_delete=models.SET_NULL, null=True, verbose_name="Publisher")
    market_id = models.PositiveIntegerField(blank=False, verbose_name="Publisher")
    discount_shop = models.PositiveSmallIntegerField(blank=False, verbose_name="Discount_shop")
    discount_market = models.PositiveSmallIntegerField(blank=False, verbose_name="Discount_market")
    available = models.BooleanField(default=False, verbose_name="Available")

    def __str__(self):
        return self.title


class PBook(Book):
    pass


class EBook(Book):
    source = models.URLField(blank=True, null=True, verbose_name="Source")


class ABook(Book):
    file = models.FileField(upload_to=None, blank=True, null=True, verbose_name="File")


class Types(models.IntegerChoices):
    ASSOCIATIVE = 1
    DIDACTIC = 2
    COMBINED = 3


class BBook(Book):
    symbol_type = models.PositiveSmallIntegerField(choices=Types.choices)


class PromoCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    percent = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Percent")
    user = models.ForeignKey(to="user.User", on_delete=models.CASCADE, verbose_name="User")
    times_to_use = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Times_to_use")
    times_used = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Times_used")

    def __str__(self):
        return self.id

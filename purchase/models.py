from django.db import models
from django.utils import timezone
from user.models import User
from book.models import Book
from django.utils import timezone


class Statuses(models.IntegerChoices):
    PROCESSED = 1
    CANCELED = 2
    ACCEPTED = 3


class Purchase(models.Model):
    user_id = models.ForeignKey(to=User, blank=False, null=True, on_delete=models.CASCADE,
                                related_name="Purchase", verbose_name="User")
    books = models.ForeignKey(to=Book, blank=False, null=True, on_delete=models.SET_NULL,
                              related_name="Purchase", verbose_name="Book")
    amount = models.DecimalField(blank=False, verbose_name="Amount")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created_at")
    status = models.PositiveSmallIntegerField(blank=False, null=True, choices=Statuses.choices,
                                              verbose_name="Status")



from book.modals import (
    Book, Category, Author, Publisher, Contract, Market, DiscountShop
)

from random import randint, choice
from string import ascii_lowercase
from django.utils import timezone

#
# def create_purchase(count):
#     def get_random_obf(model):
#         random_idx = randint(0, model.objects.count() - 1)
#         return model.objects.all()[random_idx]
#     now = timezone.now()
#
#     for item in range(count):
#         params = {
#             "user_id": get_random_obf(User),
#             "books": get_random_obf(Book),
#             "amount": randint(1, 2000),
#             "created_at": now,
#             "status": PROCESSED,
#         }
#         Book.objects.create(params)
#
#
# class Statuses(models.IntegerChoices):
#     PROCESSED = 1
#     CANCELED = 2
#     ACCEPTED = 3

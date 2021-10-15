from book.models import (
    DiscountShop, Author, Book, Publisher
)
from django.db.models import FloatField, OuterRef
from django.db.models.functions import Cast

from django.db.models import Avg, Max, F, Sum, Min

# Средняя скидка от автора Avg int
def get_avg_discount():
    author = Author.objects.first()
    return Book.objects.filter(authors=author).aggregate(Avg('discount_shop__author_discount'))


# Сколько теряет автор денег, если вводиться скидка от продавца, например процент автора 30%
def how_much_money_author_lose():
    author = Author.objects.first()
    return Book.objects.filter(authors=author)\
        .annotate(
            loses_test2=(Cast(F('price'), FloatField()) -
                         Cast(F('price'), FloatField()) *
                         Cast(F('discount_shop__shop_discount'), FloatField()) / 100) *
                         Cast(F('authors__percent'), FloatField()) / 100,
        ).aggregate(
            Sum(F('loses_test2')),
        )


def publisher_max_and_min_cost():
    return Publisher.objects.filter(
            books__in=Book.objects.annotate(min_price=Min('price')).values('id')
        ).all()


def main():
    print(get_avg_discount())
    print(how_much_money_author_lose())
    print(publisher_max_and_min_cost())

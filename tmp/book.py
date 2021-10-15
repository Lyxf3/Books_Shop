from book.models import (
    Book, Category, Author, Publisher, Contract, Market,
    DiscountShop, BBook, PBook, EBook, ABook, Types
)

from random import randint, choice, choices
from string import ascii_lowercase
from django.utils import timezone

CATEGORIES_COUNT = 1500
AUTHORS_COUNT = 1500
PUBLISHER_COUNT = 100
CONTRACT_COUNT = 100
BOOK_COUNT = 1500
DISCOUNT_SHOP = 100


def get_random_obj(model):
    random_idx = randint(0, model.objects.count() - 1)
    return model.objects.all()[random_idx]


def get_random_queryset(model):
    authors = model.objects.all().values_list('id', flat=True)
    return model.objects.filter(pk__in=choices(authors, k=3))


def get_book_type():
    return choice([PBook, EBook, ABook, BBook])


def generate_data_by_type(book_type):
    if book_type == PBook:
        return {}
    elif book_type == EBook:
        generate = f'https://{"".join(choice(ascii_lowercase) for _ in range(randint(2, 30)))}/'

        if EBook.objects.filter(source=generate).exists():
            return ''.join(choice(ascii_lowercase) for _ in range(randint(2, 30)))

        return {
            "source": generate
        }
    elif book_type == ABook:
        return {
            "file": None
        }
    elif book_type == BBook:
        return {
            "symbol_type": choice([Types.ASSOCIATIVE, Types.DIDACTIC, Types.COMBINED])
        }


def create_category(count):
    for item in range(count):
        params = {
            "title": ''.join(choice(ascii_lowercase) for _ in range(randint(2, 50)))
        }
        Category.objects.create(**params)


def create_author(count):
    for item in range(count):
        params = {
            "first_name": ''.join(choice(ascii_lowercase) for _ in range(randint(2, 30))),
            "second_name": ''.join(choice(ascii_lowercase) for _ in range(randint(2, 30))),
            'percent': randint(2, 30)
        }
        Author.objects.create(**params)


def create_publisher(count):
    for item in range(count):
        params = {
            "title": ''.join(choice(ascii_lowercase) for _ in range(randint(2, 40))),
        }
        Publisher.objects.create(**params)


def create_contract(count):

    for item in range(count):
        params = {
            "title": ''.join(choice(ascii_lowercase) for _ in range(randint(2, 100))),
            "author": get_random_obj(Author),
            'publisher': get_random_obj(Publisher)
        }
        Contract.objects.create(**params)


def create_discount_shop(count):
    for item in range(count):
        params = {
            "author_discount": randint(1, 20),
            "shop_discount": randint(1, 20),
        }
        DiscountShop.objects.create(**params)


def create_book(count):

    now = timezone.now()

    for item in range(count):
        book_type = get_book_type()
        params = {
            "title": ''.join(choice(ascii_lowercase) for _ in range(randint(10, 50))),
            "price": randint(1, 2000),
            "issued": now,
            "publisher": get_random_obj(Publisher),
            "market_id": randint(1, 2000),
            "discount_market": randint(1, 50),
            "discount_shop": get_random_obj(DiscountShop),
            "available": True,
        }
        params.update(generate_data_by_type(book_type))
        book = book_type.objects.create(**params)
        authors_queryset = get_random_queryset(Author)
        categories_queryset = get_random_queryset(Category)

        for author in authors_queryset:
            book.authors.add(author)

        for categories in categories_queryset:
            book.categories.add(categories)


def main():
    create_category(CATEGORIES_COUNT)
    create_author(AUTHORS_COUNT)
    create_publisher(PUBLISHER_COUNT)
    create_contract(CONTRACT_COUNT)
    create_discount_shop(DISCOUNT_SHOP)
    create_book(BOOK_COUNT)


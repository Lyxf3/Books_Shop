from django.contrib import admin

# Register your models here.
from book.models import (
    Book, Category, Contract, Author, Publisher, Market, PBook, EBook, ABook, Types, BBook, PromoCode
)

admin.site.register(Book)

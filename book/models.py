from django.db import models
from django.utils import timezone
import uuid


class Category(models.Model):
    title = models.CharField(max_length=100,
                             blank=False,
                             null=True,
                             verbose_name="Title")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=30,
                                  blank=True,
                                  null=True,
                                  verbose_name="First_name")
    second_name = models.CharField(max_length=30,
                                   blank=True,
                                   null=True,
                                   verbose_name="Second_name")
    percent = models.PositiveSmallIntegerField(blank=False, default=20,
                                    verbose_name="Percent")


class Publisher(models.Model):
    title = models.CharField(max_length=100,
                             blank=True,
                             null=True,
                             verbose_name="Title")

    def __str__(self):
        return self.title


class Contract(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=Author,
                               on_delete=models.CASCADE,
                               related_name="contracts",
                               verbose_name="author")
    publisher = models.ForeignKey(to=Publisher,
                                  on_delete=models.CASCADE,
                                  related_name="contracts",
                                  verbose_name="publisher")


class Market(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Title")
    location = models.CharField(max_length=100,
                                verbose_name="Location")

    def __str__(self):
        return self.title


class DiscountShop(models.Model):
    author_discount = models.PositiveSmallIntegerField(blank=False,
                                                       verbose_name="Author_discount")
    shop_discount = models.PositiveSmallIntegerField(blank=False,
                                                     verbose_name="Author_discount")

    def __str__(self):
        return f'author_discount: {self.author_discount} shop_discount:{self.shop_discount}'


class Book(models.Model):
    title = models.CharField(max_length=100,
                             blank=False,
                             null=True,
                             verbose_name="Title")
    price = models.PositiveIntegerField(blank=False,
                                        verbose_name="Price")
    issued = models.DateTimeField(default=timezone.now,
                                  verbose_name="Issued")
    categories = models.ManyToManyField(to=Category,
                                        blank=False,
                                        related_name="books",
                                        verbose_name="Categories")
    authors = models.ManyToManyField(to=Author,
                                     blank=False,
                                     related_name="books",
                                     verbose_name="Authors")
    publisher = models.ForeignKey(to=Publisher,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name="books",
                                  verbose_name="Publisher")
    market_id = models.PositiveIntegerField(blank=False,
                                            verbose_name="Market_id")
    discount_shop = models.ForeignKey(to=DiscountShop,
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      related_name="books",
                                      verbose_name="Discount_shop")
    discount_market = models.PositiveSmallIntegerField(blank=False,
                                                       verbose_name="Discount_market")
    available = models.BooleanField(default=False,
                                    verbose_name="Available")

    def __str__(self):
        return self.title

    def get_fields(self):
        return "\n".join([p.products for p in self.product.all()])

    def categories_list(self):
        return ', '.join([str(category) for category in self.categories.all()])

    categories_list.short_description="Categories"


class PBook(Book):
    pass


class EBook(Book):
    source = models.URLField(blank=True,
                             null=True,
                             unique=True,
                             verbose_name="Source")


class ABook(Book):
    file = models.FileField(upload_to=None,
                            blank=True,
                            null=True,
                            verbose_name="File")


class Types(models.IntegerChoices):
    ASSOCIATIVE = 1
    DIDACTIC = 2
    COMBINED = 3


class BBook(Book):
    symbol_type = models.PositiveSmallIntegerField(choices=Types.choices)


class PromoCode(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          verbose_name="Id")
    percent = models.PositiveSmallIntegerField(blank=True,
                                               null=True,
                                               verbose_name="Percent")
    user = models.ForeignKey(to="user.User",
                             on_delete=models.CASCADE,
                             null=True,
                             related_name='promo_codes',
                             verbose_name="User")
    times_to_use = models.PositiveSmallIntegerField(blank=True,
                                                    null=True,
                                                    verbose_name="Times_to_use")
    times_used = models.PositiveSmallIntegerField(blank=True,
                                                  null=True,
                                                  verbose_name="Times_used")

    def __str__(self):
        return self.id

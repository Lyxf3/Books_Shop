from django.contrib import admin
from django.db.models import OuterRef
from django.utils.html import mark_safe
from book.models import (
    Book, Category, Contract, Author, Publisher, DiscountShop,
    Market, PBook, EBook, ABook, Types, BBook, PromoCode
)
from django.utils.html import format_html

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'issued', 'market_id',
                    'discount_market', 'available', 'discount_shop',
                    'categories_list', 'publisher_name', ]
    search_fields = ('title', 'price')
    fields = ('title', 'price', 'discount_shop')
    readonly_fields = ('issued', 'market_id', 'discount_market', 'available', 'categories_list',)

    def get_queryset(self, request):
        query_set = super(BookAdmin, self).get_queryset(request)

        return query_set \
            .annotate(_publisher_name= \
                          Publisher.objects.filter(
                              id=OuterRef('publisher_id')
                          ).values('title')
                      ) \
            .select_related('discount_shop') \
            .prefetch_related('categories')

    def publisher_name(self, instance):
        return instance._publisher_name


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ('title',)
    readonly_fields = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'percent']
    search_fields = ('second_name',)
    readonly_fields = ('first_name', 'second_name', 'percent')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ('title',)
    readonly_fields = ('title',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher']
    search_fields = ('title', 'author', 'publisher')
    readonly_fields = ('title', 'author', 'publisher')

    def get_queryset(self, request):
        query_set = super(ContractAdmin, self).get_queryset(request)
        return query_set \
            .select_related('author') \
            .select_related('publisher')


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ['title', 'location']
    search_fields = ('title',)
    readonly_fields = ('title', 'location')


@admin.register(DiscountShop)
class DiscountShopAdmin(admin.ModelAdmin):
    list_display = ['author_discount', 'shop_discount']
    search_fields = ('author_discount', 'shop_discount')
    fields = ('author_discount', 'shop_discount',)


@admin.register(EBook)
class EBookAdmin(BookAdmin):
    def get_list_display(self, request):
        return self.list_display + ['source']

    def get_search_fields(self, request):
        return self.search_fields + ('source', )

    def get_readonly_fields(self, request):
        return self.readonly_fields + ('source', )


@admin.register(ABook)
class ABookAdmin(BookAdmin):
    def get_list_display(self, request):
        return self.list_display + ['file', ]

    def get_search_fields(self, request):
        return self.search_fields + ('file', )

    def get_readonly_fields(self, request):
        return self.readonly_fields + ('file', )


@admin.register(BBook)
class BBookAdmin(BookAdmin):
    def get_list_display(self, request):
        return self.list_display + ['symbol_type']

    def get_search_fields(self, request):
        return self.search_fields + ('symbol_type', )

    def get_readonly_fields(self, request):
        return self.readonly_fields + ('symbol_type', )


@admin.register(PBook)
class PBookAdmin(BookAdmin):
    def get_list_display(self, request):
        return self.list_display

    def get_search_fields(self, request):
        return self.search_fields

    def get_readonly_fields(self, request):
        return self.readonly_fields


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'percent', 'user', 'times_to_use', 'times_used', ]
    search_fields = ('id', 'user')
    readonly_fields = ('id', 'percent', 'user', 'times_to_use', 'times_used',)

    def get_queryset(self, request):
        query_set = super(PromoCodeAdmin, self).get_queryset(request)
        return query_set \
            .select_related('user')

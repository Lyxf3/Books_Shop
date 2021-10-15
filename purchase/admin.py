from django.contrib import admin
from django.utils.html import mark_safe

from purchase.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'books', 'amount',
                    'created_at', 'status')
    search_fields = ('user_id',)
    list_filter = ('status',)
    fields = ()
    readonly_fields = ('user_id', 'books', 'amount',
                       'created_at', 'status')

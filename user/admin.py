from django.contrib import admin
from django.utils.html import mark_safe

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_staff', 'is_superuser',
                    'is_active', 'balance', 'date_joined')
    search_fields = ('email', 'name')
    list_filter = ('is_superuser', 'is_active', 'is_staff')
    fields = ('name', 'balance',)
    readonly_fields = ('email', 'is_staff', 'is_superuser',
                       'is_active', 'date_joined')

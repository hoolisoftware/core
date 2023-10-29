from django.contrib import admin

from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'username',
        'updated',
        'created'
    )
    search_fields = ('username', 'full_name')

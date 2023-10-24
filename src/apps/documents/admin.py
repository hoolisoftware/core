from django.contrib import admin

from . import models


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )

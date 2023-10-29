from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


from . import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'code',
    )


@admin.register(models.PaymentMethod)
class PaymentMethodAdmin(DraggableMPTTAdmin):
    list_display = (
        'indented_title',
    )
    list_display_links = (
        'indented_title',
    )
    search_fields = ('name', )


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'period',
        'amount',
        'method',
        'created',
    )
    autocomplete_fields = ('method', )

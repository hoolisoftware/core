from django.contrib import admin

from . import models


@admin.register(models.PaymentCurrecy)
class PaymentCurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code'
    )


@admin.register(models.PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'currency'
    )


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'method',
        'amount',
        'created'
        # TODO Order
    )

from django.contrib import admin

from . import models


@admin.register(models.MarketPlace)
class MarketPlaceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'comission'
    )


@admin.register(models.MarketPlaceAccount)
class MarketPlaceAccountAdmin(admin.ModelAdmin):
    list_display = (
        'marketplace',
        'username'
    )

from django.contrib import admin

from . import models


class MarketPlaceAccountInline(admin.TabularInline):
    model = models.MarketPlaceAccount
    exclude = ('note', )


@admin.register(models.MarketPlace)
class MarketPlaceAdmin(admin.ModelAdmin):
    inlines = (MarketPlaceAccountInline, )
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

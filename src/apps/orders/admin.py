from django.contrib import admin

from . import models


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class PeriodInline(admin.TabularInline):
    model = models.Period


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ('project', )
    inlines = (
        PeriodInline,
    )
    list_display = (
        'project',
        'budget',
        'starting_from',
        'deadline',
        'production',
    )


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'hours',
        'hour_rate',
        'executor'
    )

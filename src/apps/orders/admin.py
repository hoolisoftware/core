from django.contrib import admin

from . import models
from ..payments.models import Payment


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('name', )
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
    autocomplete_fields = ('executor', )


class PaymentInline(admin.TabularInline):
    model = Payment


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            'Поэзия',
            {
                "fields": ['project', 'title', 'note'],
            },
        ),
        (
            'Даты',
            {
                'fields': ['starting_from', 'deadline'],
            },
        ),
        (
            'Условия',
            {
                'classes': ['collapse'],
                'fields': ['broker', 'broker_comission', 'policies'],
            },
        ),
        (
            'Финал',
            {
                'classes': ['collapse'],
                'fields': ['production', 'archived'],
            },
        ),
    ]
    autocomplete_fields = ('project', )
    search_fields = ('project__name', )
    inlines = (
        PeriodInline,
        PaymentInline
    )
    list_display = (
        'title',
        'id',
        'project',
        'starting_from',
        'deadline',
        '_price',
        '_hours'
    )

    @admin.display(description='Стоимость')
    def _price(self, obj):
        return f'{obj.price} $'

    @admin.display(description='Время')
    def _hours(self, obj):
        return f'{sum([int(i.minutes/60) for i in obj.work_sessions.all()])} / {obj.hours}' # noqa


@admin.register(models.OrderActive)
class OrderActiveAdmin(OrderAdmin):

    def get_queryset(self, request):
        return super().get_queryset(request).filter(archived=False)


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'hours',
        'hour_rate',
        'executor'
    )

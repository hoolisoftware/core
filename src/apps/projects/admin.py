from django.contrib import admin

from . import models
from ..payments.models import Payment


class RepositoryInline(admin.TabularInline):
    model = models.Repository


class ProjectDocumentInline(admin.TabularInline):
    exclude = ('description', )
    show_change_link = True
    model = models.ProjectDocument


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (
        RepositoryInline,
        ProjectDocumentInline
    )
    list_display = (
        'customer',
        'title',
        'updated',
        'created'
    )
    search_fields = ('title', )
    autocomplete_fields = ('customer',)


class PeriodInline(admin.TabularInline):
    autocomplete_fields = ('executor', 'order', 'service')
    exclude = ('executor', 'hour_rate', 'hours', 'technical_task')
    model = models.Period


class PaymentInline(admin.TabularInline):
    model = Payment


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Поэзия', {
            "fields": ['project', 'title', 'note'],
        }),
        ('Даты', {
            'fields': ['starting_from', 'deadline'],
        }),
        ('Условия', {
            'classes': ['collapse'],
            'fields': ['broker', 'broker_comission', 'policies'],
        }),
        ('Финал', {
            'classes': ['collapse'],
            'fields': ['production', 'archived'],
        }),
    ]
    autocomplete_fields = ('project', )
    search_fields = ('project__name', )
    inlines = (
        PeriodInline,
    )
    list_display = (
        'title',
        'id',
        'project',
        'starting_from',
        'deadline',
    )


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    inlines = (
        PaymentInline,
    )
    list_display = (
        'order',
        'service',
        'hours',
        'hour_rate',
        'executor',
    )
    search_fields = (
        'order__project__title',
        'order__title',
        'name'
    )
    autocomplete_fields = ('executor', 'order', 'service')

from django.contrib import admin

from . import models


@admin.register(models.WorkSessionReport)
class WorkSessionReportAdmin(admin.ModelAdmin):
    list_display = (
        'minutes',
        'executor',
        'order',
        'created'
    )
    autocomplete_fields = ('executor', 'order')

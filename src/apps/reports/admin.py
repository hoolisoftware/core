from django.contrib import admin

from . import models


@admin.register(models.WorkSessionReport)
class WorkSessionReportAdmin(admin.ModelAdmin):
    list_display = (
        'minutes',
        'created'
    )
    autocomplete_fields = ('period', )

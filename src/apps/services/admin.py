from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin
from django.utils.html import format_html

from . import models


@admin.register(models.Service)
class ServiceAdmin(DraggableMPTTAdmin):
    search_fields = (
        'name__icontains',
        'parent__name',
    )
    list_display = (
        '_name',
    )
    list_display_links = ('_name', )
    mptt_level_indent = 50
    autocomplete_fields = ('parent', )

    def _name(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,  # Or whatever you want to put here
        )


@admin.register(models.Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

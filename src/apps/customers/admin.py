from django.contrib import admin

from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'username',
        'updated',
        'created'
    )
    search_fields = ('username', 'full_name')


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'title',
        'updated',
        'created'
    )
    autocomplete_fields = ('documents', 'customer')

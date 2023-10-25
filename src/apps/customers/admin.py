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


class RepositoryInline(admin.TabularInline):
    model = models.Repository


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (
        RepositoryInline,
    )
    list_display = (
        'customer',
        'title',
        'updated',
        'created'
    )
    search_fields = ('title', )
    autocomplete_fields = ('documents', 'customer')

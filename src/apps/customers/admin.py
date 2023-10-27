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

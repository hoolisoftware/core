from django.contrib import admin

from . import models


@admin.register(models.OrderActive)
class OrderActiveAdmin(admin.ModelAdmin):
    list_display = ('title', )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(archived=False)


class WorkSessionReportInline(admin.TabularInline):
    model = models.MyWorkSessionReport


@admin.register(models.MyPeriodProcess)
class MyPeriodProcessAdmin(admin.ModelAdmin):
    inlines = (WorkSessionReportInline,)
    list_display = ('name', 'hours', '_hours_spent')
    readonly_fields = (
        'order',
        'name',
        'hour_rate',
        'hours',
        'executor',
        'service',
        'technical_task',
    )

    @admin.display(description='Потрачено часов')
    def _hours_spent(self, obj):
        return sum([o.minutes/60 for o in obj.work_sessions.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).filter(status='process')


@admin.register(models.MyPeriodTodo)
class MyPeriodTodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'hours')

    def get_queryset(self, request):
        return super().get_queryset(request).filter(status='todo')


@admin.register(models.MyWorkSessionReport)
class MyWorkSessionReportAdmin(admin.ModelAdmin):
    list_display = ('minutes', 'period')
    autocomplete_fields = ('period', )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(period__executor=request.user) # noqa

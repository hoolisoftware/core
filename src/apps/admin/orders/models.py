from ...projects.models import Order, Period
from ...reports.models import WorkSessionReport


class OrderActive(Order): # noqa ignore DJ08
    class Meta:
        proxy = True
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы (активные)'


class MyPeriodProcess(Period): # noqa ignore DJ08
    class Meta:
        proxy = True
        verbose_name = 'Мой период (в процессе)'
        verbose_name_plural = 'Мои периоды (в процессе)'


class MyPeriodTodo(Period): # noqa ignore DJ08
    class Meta:
        proxy = True
        verbose_name = 'Мой период (будущий)'
        verbose_name_plural = 'Мои периоды (будущие)'


class MyWorkSessionReport(WorkSessionReport): # noqa ignore DJ08
    class Meta:
        proxy = True
        verbose_name = 'Моя рабочая сессия'
        verbose_name_plural = 'Мои рабочие сесии'

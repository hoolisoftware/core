from django.contrib.auth import get_user_model
from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin
from apps.orders.models import Order


User = get_user_model()


class WorkSessionReport(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Рабочая сессия'
        verbose_name_plural = 'Рабочие сессии'

    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='work_sessions') # noqa
    minutes = models.PositiveIntegerField('Кол-во минут')
    executor = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE, related_name='work_sessions') # noqa

    def __str__(self):
        return f'[{self.executor.username}, {self.minutes}] {self.order}'

from django.db import models

from mixins.model_mixins import DateTimeCreatedUpdatedModelMixin
from apps.orders.models import Order


class PaymentCurrecy(models.Model):
    class Meta:
        verbose_name = 'Валюта оплаты'
        verbose_name_plural = 'Валюты оплаты'

    name = models.CharField('Название', max_length=64)
    code = models.CharField('Код', max_length=8)

    def __str__(self):
        return f'{self.name} ({self.code})'


class PaymentMethod(models.Model):
    class Meta:
        verbose_name = 'Метод оплаты'
        verbose_name_plural = 'Методы оплаты'

    currency = models.ForeignKey(PaymentCurrecy, verbose_name='Валюта оплаты', on_delete=models.CASCADE) # noqa
    name = models.CharField('Название', max_length=64)
    requisites = models.TextField('Реквизиты', blank=True)

    def __str__(self):
        return f'{self.name} {self.currency}'


class Payment(DateTimeCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    method = models.ForeignKey(PaymentMethod, verbose_name='Метод оплаты', on_delete=models.CASCADE) # noqa ignore
    amount = models.PositiveIntegerField('Сумма')
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.SET_NULL, null=True) # noqa

    def __str__(self):
        return f'{self.amount} {self.method.currency}'

from mptt.models import MPTTModel, TreeForeignKey
from django.db import models

from mixins.model_mixins import DateTimeCreatedUpdatedModelMixin
from apps.projects.models import Period


class Currency(models.Model):
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ('code', )

    code = models.CharField('Код валюты', max_length=16)

    def __str__(self):
        return self.code


class PaymentMethod(MPTTModel):
    class Meta:
        verbose_name = 'Метод оплаты'
        verbose_name_plural = 'Методы оплаты'

    parent = TreeForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, null=True, blank=True, related_name='children') # noqa
    currency = models.ForeignKey(Currency, verbose_name='Валюта', on_delete=models.CASCADE, related_name='methods', null=True, blank=True) # noqa
    name = models.CharField('Название', max_length=64)
    requisites = models.TextField('Реквизиты', blank=True)

    def __str__(self):
        return ' / '.join([i.name for i in self.get_ancestors(include_self=True)]) # noqa


class Payment(DateTimeCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    method = models.ForeignKey(PaymentMethod, verbose_name='Метод оплаты', on_delete=models.CASCADE) # noqa ignore
    amount = models.PositiveIntegerField('Сумма')
    period = models.ForeignKey(Period, verbose_name='Период', on_delete=models.CASCADE) # noqa

    def __str__(self):
        return f'{self.amount} {self.method.currency}'

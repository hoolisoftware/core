from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin


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
    requisites = models.TextField('Реквизиты', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.currency}'


class Payment(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    method = models.ForeignKey(PaymentMethod, verbose_name='Метод оплаты', on_delete=models.CASCADE) # noqa ignore
    amount = models.PositiveIntegerField('Сумма')
    order = None  # TODO Order

    def __str__(self):
        return f'{self.amount} {self.method.currency}'

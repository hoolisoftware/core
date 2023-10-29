from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin
from apps.marketplaces.models import MarketPlace


class Customer(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    channel = models.ForeignKey(MarketPlace, verbose_name='Канал', on_delete=models.SET_NULL, null=True, blank=True) # noqa
    full_name = models.CharField('ИФО', max_length=128)
    username = models.CharField('Никнейм', max_length=64, unique=True) # noqa
    contact_info = models.TextField('Контактная информация', blank=True, null=True) # noqa

    def __str__(self):
        return f'@{self.username} {self.full_name}'

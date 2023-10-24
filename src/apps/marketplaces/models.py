from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin


class MarketPlace(models.Model):
    class Meta:
        verbose_name = 'Маркетплейс'
        verbose_name_plural = 'Маркетплейсы'

    name = models.CharField('Название', max_length=32)
    comission = models.PositiveIntegerField('Комиссионный сбор (%)', help_text='Выражается в процентах') # noqa

    def __str__(self):
        return self.name


class MarketPlaceAccount(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Учётная запись'
        verbose_name_plural = 'Учётные записи'

    marketplace = models.ForeignKey(MarketPlace, verbose_name='Маркетплейс', on_delete=models.CASCADE) # noqa
    username = models.CharField('Никнейм', max_length=128, help_text='Почта, номер телефона, имя пользователя - короче говоря логин') # noqa
    note = models.TextField('Заметка', blank=True, null=True, help_text='Не рекомендуется оставлять сюда пароли и другую конфиденциальную информацию') # noqa

    def __str__(self):
        return f'{self.marketplace.name} / {self.username}'

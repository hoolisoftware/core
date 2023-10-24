from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin
from apps.documents.models import Document


class Customer(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    channel = None  # TODO MarketPlace
    full_name = models.CharField('ИФО', max_length=128)
    username = models.CharField('Никнейм', max_length=64, unique=True) # noqa
    contact_info = models.TextField('Контактная информация', blank=True, null=True) # noqa

    def __str__(self):
        return f'{self.full_name} @{self.username}'


class Project(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    customer = models.ForeignKey(Customer, verbose_name='Заказчик', on_delete=models.SET_NULL, blank=True, null=True) # noqa
    title = models.CharField('Заголовок', max_length=64)
    repository = models.URLField('Ссылка на репозиторий', blank=True, null=True) # noqa
    description = models.TextField('Короткое описание', blank=True)
    documents = models.ManyToManyField(Document, verbose_name='Документы', blank=True) # noqa

    def __str__(self):
        return f'#{self.id} - {self.title}'

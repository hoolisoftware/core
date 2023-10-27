from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin
from apps.marketplaces.models import MarketPlace
from apps.documents.models import Document


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


class Project(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    customer = models.ForeignKey(Customer, verbose_name='Заказчик', on_delete=models.SET_NULL, blank=True, null=True) # noqa
    title = models.CharField('Заголовок', max_length=64)
    description = models.TextField('Короткое описание', blank=True)

    def __str__(self):
        return f'#{self.id} - {self.title}'


class ProjectDocument(Document):
    class Meta:
        verbose_name = 'Документ проекта'
        verbose_name_plural = 'Документы проекта'

    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, related_name='documents') # noqa


class Repository(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Репозиторий'
        verbose_name_plural = 'Репозитории'

    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE) # noqa
    link = models.URLField('Ссылка на репозиторий')

    def __str__(self):
        return self.link

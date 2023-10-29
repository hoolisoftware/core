from mixins.model_mixins import DateCreatedUpdatedModelMixin
from django.db import models
from django.contrib.auth import get_user_model

from apps.customers.models import Customer
from apps.documents.models import Document
from apps.services.models import Policy, Service
from . import help_text


User = get_user_model()


class Project(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    customer = models.ForeignKey(Customer, verbose_name='Заказчик', on_delete=models.SET_NULL, blank=True, null=True) # noqa
    title = models.CharField('Заголовок', max_length=64)
    description = models.TextField('Короткое описание', blank=True)

    def __str__(self):
        return self.title


class Repository(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Репозиторий'
        verbose_name_plural = 'Репозитории'

    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE) # noqa
    link = models.URLField('Ссылка на репозиторий')

    def __str__(self):
        return self.link


class ProjectDocument(Document):
    class Meta:
        verbose_name = 'Документ проекта'
        verbose_name_plural = 'Документы проектов'

    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE, related_name='documents') # noqa


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    title = models.CharField('Заголовок', max_length=64)
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE) # noqa
    broker = models.ForeignKey(User, verbose_name='Посредник', on_delete=models.SET_NULL, blank=True, null=True) # noqa
    broker_comission = models.PositiveIntegerField('Комиссия посредника (%)', default=20) # noqa
    policies = models.ManyToManyField(Policy, verbose_name='Политики', help_text=help_text.order_policy) # noqa

    starting_from = models.DateField('Дата начала', blank=True, null=True)
    deadline = models.DateField('Дедлайн', blank=True, null=True)
    production = models.DateField('Продакшн', blank=True, null=True)
    note = models.TextField('Заметка', blank=True)

    archived = models.BooleanField('В архиве', default=False)

    def __str__(self):
        return f'{getattr(self.project, "title", None)} / {self.title}' # noqa


class Period(models.Model):
    STATUS = (
        ('todo', 'Предстоит выполнить'),
        ('process', 'Выполняется'),
        ('done', 'Выполнен')
    )

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    name = models.CharField('Название', max_length=64)
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='periods') # noqa
    executor = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE) # noqa
    hours = models.PositiveIntegerField('Кол-во часов', blank=True, null=True)
    hour_rate = models.PositiveIntegerField('Ставка в час ($)')
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.SET_NULL, null=True, blank=True) # noqa
    technical_task = models.FileField('Техническое задание', upload_to='projects/period/technical_task/%Y/%m/%d/', blank=True) # noqa
    status = models.CharField('Статус', choices=STATUS, default='todo', max_length=16) # noqa

    def __str__(self):
        return f'{self.order.project} / {self.order.title} / {self.name}'

from django.db import models
from django.contrib.auth import get_user_model

from apps.customers.models import Project


User = get_user_model()


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    name = models.CharField('Название', max_length=64)
    specification = models.FileField('Спецификация', upload_to='orders/service/specification/%Y/%m/%d/', blank=True) # noqa

    def __str__(self):
        return self.name


class Policy(models.Model):
    class Meta:
        verbose_name = 'Политика'
        verbose_name_plural = 'Политики'

    name = models.CharField('Заголовок', max_length=128)
    specification = models.FileField('Спецификация', upload_to='orders/policy/specification/%Y/%m/%d/', blank=True) # noqa

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.SET_NULL, null=True) # noqa
    broker = models.ForeignKey(User, verbose_name='Посредник', on_delete=models.SET_NULL, blank=True, null=True) # noqa
    broker_comission = models.PositiveIntegerField('Комиссия посредника (%)', default=20) # noqa
    services = models.ManyToManyField(Service, verbose_name='Услуги')
    policies = models.ManyToManyField(Policy, verbose_name='Политики')

    budget = models.PositiveIntegerField('Бюджет', blank=True)
    starting_from = models.DateField('Дата начала')
    deadline = models.DateField('Дедлайн')
    production = models.DateField('Продакшн', blank=True)
    note = models.TextField('Заметка', blank=True)

    archived = models.BooleanField('В архиве', default=False)

    def __str__(self):
        return f'{getattr(self.project, "title", None)} #{self.id}'


class Period(models.Model):
    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    hours = models.FloatField('Кол-во часов')
    hour_rate = models.PositiveIntegerField('Ставка в час ($)')
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE) # noqa
    executor = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE) # noqa
    technical_task = models.FileField('Техническое задание', upload_to='orders/period/technical_task/%Y/%m/%d/', blank=True) # noqa

    def __str__(self):
        return f'{self.executor.username} #{self.order.id} {self.hours}'

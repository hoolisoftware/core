from django.db import models
from django.contrib.auth import get_user_model

from apps.customers.models import Project
from . import help_text


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

    title = models.CharField('Заголовок', max_length=64)
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.SET_NULL, null=True) # noqa
    broker = models.ForeignKey(User, verbose_name='Посредник', on_delete=models.SET_NULL, blank=True, null=True) # noqa
    broker_comission = models.PositiveIntegerField('Комиссия посредника (%)', default=20) # noqa
    policies = models.ManyToManyField(Policy, verbose_name='Политики', help_text=help_text.order_policy) # noqa

    starting_from = models.DateField('Дата начала', blank=True, null=True)
    deadline = models.DateField('Дедлайн', blank=True, null=True)
    production = models.DateField('Продакшн', blank=True, null=True)
    note = models.TextField('Заметка', blank=True)

    archived = models.BooleanField('В архиве', default=False)

    def __str__(self):
        return f'{getattr(self.project, "title", None)} #{self.id} ({self.title})' # noqa

    @property
    def price(self):
        return sum([period.hours*period.hour_rate for period in self.periods.all()]) # noqa

    @property
    def hours(self):
        return sum([period.hours for period in self.periods.all()])


class OrderActive(Order): # noqa DJ08
    class Meta:
        proxy = True
        verbose_name = 'Активный заказ'
        verbose_name_plural = 'Активные заказы'


class Period(models.Model):
    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='periods') # noqa
    executor = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE) # noqa
    hours = models.PositiveIntegerField('Кол-во часов')
    hour_rate = models.PositiveIntegerField('Ставка в час ($)')
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.SET_NULL, null=True, blank=True) # noqa
    technical_task = models.FileField('Техническое задание', upload_to='orders/period/technical_task/%Y/%m/%d/', blank=True) # noqa

    def __str__(self):
        return f'{self.executor.username} #{self.order.id} {self.hours}'

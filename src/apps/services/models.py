from mptt.models import MPTTModel, TreeForeignKey
from django.db import models


class Service(MPTTModel):
    class Meta:
        verbose_name = 'Категория Услуг'
        verbose_name_plural = 'Категории Услуг'

    mptt_indent_field = "name"
    parent = TreeForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, null=True, blank=True, related_name='children') # noqa
    name = models.CharField('Название', max_length=64)
    specification = models.FileField('Спецификация', upload_to='services/service/specification/%Y/%m/%d/', blank=True) # noqa

    def __str__(self):
        return self.name


class Policy(models.Model):
    class Meta:
        verbose_name = 'Политика'
        verbose_name_plural = 'Политики'

    name = models.CharField('Заголовок', max_length=128)
    specification = models.FileField('Спецификация', upload_to='services/policy/specification/%Y/%m/%d/', blank=True) # noqa

    def __str__(self):
        return self.name

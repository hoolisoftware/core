from django.db import models


class DateCreatedUpdatedModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateField('Создано', auto_now_add=True)
    updated = models.DateField('Обновлено', auto_now=True)


class DateTimeCreatedUpdatedModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField('Создано', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)

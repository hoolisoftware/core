from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin


class Document(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    name = models.CharField('Название документа', max_length=64)
    file = models.FileField('Документ', upload_to='documents/document/file/%Y/%m/%d/') # noqa
    description = models.TextField('Описание документа', blank=True)

    def __str__(self):
        return f'{self.name} ({self.created})'

from django.contrib.auth import get_user_model
from django.db import models

from mixins.model_mixins import DateCreatedUpdatedModelMixin
from apps.projects.models import Period


User = get_user_model()


class WorkSessionReport(DateCreatedUpdatedModelMixin):
    class Meta:
        verbose_name = 'Рабочая сессия'
        verbose_name_plural = 'Рабочие сессии'

    period = models.ForeignKey(Period, verbose_name='Период', on_delete=models.CASCADE, related_name='work_sessions') # noqa
    minutes = models.PositiveIntegerField('Кол-во минут')
    report = models.FileField('Отчёт', upload_to='reports/work_session_report/report/', null=True, blank=True) # noqa

    def __str__(self):
        return f'{self.minutes} - {self.period}'

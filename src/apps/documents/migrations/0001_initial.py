# Generated by Django 4.2.6 on 2023-10-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateField(auto_now=True, verbose_name='Обновлено')),
                ('name', models.CharField(max_length=64, verbose_name='Название документа')),
                ('file', models.FileField(upload_to='documents/document/file/%Y/%m/%d/', verbose_name='Документ')),
                ('description', models.TextField(blank=True, verbose_name='Описание документа')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]

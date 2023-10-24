# Generated by Django 4.2.6 on 2023-10-24 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создано'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]
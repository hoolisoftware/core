# Generated by Django 4.2.6 on 2023-10-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Короткое описание'),
        ),
    ]

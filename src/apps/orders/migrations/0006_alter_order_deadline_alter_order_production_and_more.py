# Generated by Django 4.2.6 on 2023-10-26 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_budget_alter_order_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Дедлайн'),
        ),
        migrations.AlterField(
            model_name='order',
            name='production',
            field=models.DateField(blank=True, null=True, verbose_name='Продакшн'),
        ),
        migrations.AlterField(
            model_name='order',
            name='starting_from',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_title_alter_order_policies_alter_period_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderActive',
            fields=[
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Активные заказы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('orders.order',),
        ),
        migrations.RemoveField(
            model_name='order',
            name='budget',
        ),
    ]
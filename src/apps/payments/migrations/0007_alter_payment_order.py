# Generated by Django 4.2.6 on 2023-10-26 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_title_alter_order_policies_alter_period_hours'),
        ('payments', '0006_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='orders.order', verbose_name='Заказ'),
        ),
    ]

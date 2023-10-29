# Generated by Django 4.2.6 on 2023-10-29 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_currency_alter_paymentmethod_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='currency',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='methods', to='payments.currency', verbose_name='Валюта'),
            preserve_default=False,
        ),
    ]
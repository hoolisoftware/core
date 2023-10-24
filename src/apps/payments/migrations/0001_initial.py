# Generated by Django 4.2.6 on 2023-10-24 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCurrecy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'Валюта оплаты',
                'verbose_name_plural': 'Валюты оплаты',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('requisites', models.TextField(verbose_name='Реквизиты')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.paymentcurrecy', verbose_name='Валюта оплаты')),
            ],
            options={
                'verbose_name': 'Метод оплаты',
                'verbose_name_plural': 'Методы оплаты',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Сумма')),
                ('method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.paymentmethod', verbose_name='Метод оплаты')),
            ],
            options={
                'verbose_name': 'Транзакции',
            },
        ),
    ]

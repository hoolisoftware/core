# Generated by Django 4.2.6 on 2023-10-26 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_document_file'),
        ('orders', '0004_alter_period_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='budget',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Бюджет'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateField(blank=True, verbose_name='Дедлайн'),
        ),
        migrations.AlterField(
            model_name='order',
            name='starting_from',
            field=models.DateField(blank=True, verbose_name='Дата начала'),
        ),
        migrations.CreateModel(
            name='TechnicalTask',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='documents.document')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Техническое задание',
                'verbose_name_plural': 'Технические задания',
            },
            bases=('documents.document',),
        ),
    ]
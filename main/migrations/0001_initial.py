# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('in_stock', 'Доступний на складі'), ('hired', 'У прокаті'), ('needs_repairs', 'Потребує ремонту'), ('under_repair', 'У ремонті')], max_length=24, null=True, verbose_name='Статус')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Обладнання',
                'verbose_name_plural': 'Обладнаня',
            },
        ),
    ]

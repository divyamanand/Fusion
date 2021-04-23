# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-23 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0002_auto_20191101_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_bill',
            name='month',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='monthly_bill',
            name='year',
            field=models.IntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='payments',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]

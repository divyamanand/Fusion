# Generated by Django 2.2.9 on 2020-02-03 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0002_auto_20191101_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_bill',
            name='month',
            field=models.CharField(default=2, max_length=20),
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

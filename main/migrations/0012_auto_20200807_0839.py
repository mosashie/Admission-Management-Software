# Generated by Django 3.1 on 2020-08-07 07:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200807_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedstd',
            name='Entry_Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 7, 39, 47, 992061, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='Entry_Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 7, 7, 39, 47, 990107, tzinfo=utc)),
        ),
    ]

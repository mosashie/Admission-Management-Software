# Generated by Django 2.2.2 on 2019-07-07 08:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190707_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedstd',
            name='Entry_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 8, 35, 39, 592796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='Entry_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 8, 35, 39, 592796, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.1.4 on 2021-03-19 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0034_merge_20210131_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 8, 24, 15, 659585, tzinfo=utc)),
        ),
    ]

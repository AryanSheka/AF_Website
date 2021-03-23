# Generated by Django 3.1.4 on 2021-03-22 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0043_auto_20210322_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticcontent',
            name='sand_art_form',
            field=models.BooleanField(default=False, help_text='Check if we recruitments form is to be displayed', verbose_name='Recruitment form open'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 18, 30, 2, 185320, tzinfo=utc)),
        ),
    ]

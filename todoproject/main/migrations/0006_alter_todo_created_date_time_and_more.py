# Generated by Django 4.0.6 on 2022-08-04 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_todo_created_date_time_alter_todo_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 14, 22, 45, 416601, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='target_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 14, 22, 45, 416601, tzinfo=utc)),
        ),
    ]

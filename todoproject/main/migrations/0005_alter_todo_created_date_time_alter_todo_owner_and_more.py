# Generated by Django 4.0.6 on 2022-08-04 14:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_todo_created_date_time_alter_todo_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 14, 22, 11, 871296, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='target_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 14, 22, 11, 871296, tzinfo=utc)),
        ),
    ]

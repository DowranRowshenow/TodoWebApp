# Generated by Django 4.0.6 on 2022-07-06 08:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_favorite', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_date_time', models.DateTimeField(default=datetime.datetime(2022, 7, 6, 8, 12, 31, 560642, tzinfo=utc))),
                ('target_date', models.DateField(default=datetime.datetime(2022, 7, 6, 8, 12, 31, 560642, tzinfo=utc))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.2.19 on 2023-07-16 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_scheduler_app', '0023_scheduled_schedule_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduled',
            name='schedule_date_day',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]

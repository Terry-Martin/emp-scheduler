# Generated by Django 3.2.19 on 2023-06-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_scheduler_app', '0004_auto_20230616_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_details',
            name='name_tag',
            field=models.CharField(default='top_title', max_length=200),
        ),
    ]

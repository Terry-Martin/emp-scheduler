# Generated by Django 3.2.19 on 2023-06-21 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emp_scheduler_app', '0014_alter_shift_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='added_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

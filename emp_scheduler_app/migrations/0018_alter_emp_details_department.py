# Generated by Django 3.2.19 on 2023-06-24 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_scheduler_app', '0017_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_details',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_scheduler_app.department'),
        ),
    ]

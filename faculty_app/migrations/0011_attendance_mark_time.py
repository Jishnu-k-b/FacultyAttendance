# Generated by Django 4.2.1 on 2023-05-04 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0010_attendance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='mark_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
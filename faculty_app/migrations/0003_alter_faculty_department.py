# Generated by Django 4.2 on 2023-04-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_app', '0002_alter_faculty_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('MCA', 'Computer Application'), ('MBA', 'Business Administration'), ('ME', 'Mechanical Engineering'), ('CE', 'Civil Engineering')], max_length=3),
        ),
    ]

# Generated by Django 5.0 on 2023-12-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_time',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
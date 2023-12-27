# Generated by Django 5.0 on 2023-12-27 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('description', models.TextField()),
                ('date_time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('due_date', models.DateField()),
                ('priority', models.CharField(choices=[('high', 'HIGH'), ('medium', 'MEDIUM'), ('low', 'LOW')], default='low', max_length=20)),
                ('completion_time', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-12-03 06:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_alter_done_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

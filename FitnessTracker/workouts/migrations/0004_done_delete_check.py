# Generated by Django 5.1.2 on 2024-12-02 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('set', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workout_set', to='workouts.set')),
            ],
        ),
        migrations.DeleteModel(
            name='Check',
        ),
    ]

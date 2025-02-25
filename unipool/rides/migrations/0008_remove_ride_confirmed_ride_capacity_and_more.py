# Generated by Django 5.1.6 on 2025-02-21 18:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0007_ride_passengers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='ride',
            name='capacity',
            field=models.PositiveIntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driven_rides', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ride',
            name='pickup_location',
            field=models.CharField(default='Not specified', max_length=255),
        ),
        migrations.AlterField(
            model_name='ride',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ride',
            name='time',
            field=models.TimeField(),
        ),
    ]

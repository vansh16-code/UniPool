# Generated by Django 5.1.6 on 2025-02-21 18:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0006_ride_confirmed_alter_ride_available_seats_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='passengers',
            field=models.ManyToManyField(blank=True, related_name='booked_rides', to=settings.AUTH_USER_MODEL),
        ),
    ]

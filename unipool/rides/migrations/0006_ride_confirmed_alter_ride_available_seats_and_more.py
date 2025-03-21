# Generated by Django 5.1.6 on 2025-02-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0005_alter_ride_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ride',
            name='available_seats',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ride',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]

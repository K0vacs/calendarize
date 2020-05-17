# Generated by Django 3.0.1 on 2020-01-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_bookings_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='time',
        ),
        migrations.AddField(
            model_name='bookings',
            name='dates',
            field=models.CharField(default=None, max_length=100),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-30 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0014_auto_20200130_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='timeEnd',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='timeStart',
            new_name='start_time',
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0023_auto_20200426_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='date',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]

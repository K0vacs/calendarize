# Generated by Django 2.2.7 on 2019-11-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20191107_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersprice',
            name='customer_id',
            field=models.IntegerField(default=None),
        ),
    ]

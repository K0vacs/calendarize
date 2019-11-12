# Generated by Django 2.2.7 on 2019-11-06 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn_number', models.CharField(max_length=13)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Services')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]

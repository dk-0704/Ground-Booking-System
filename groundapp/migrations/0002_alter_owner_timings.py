# Generated by Django 3.2.7 on 2022-05-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groundapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='timings',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 3.0.6 on 2020-07-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200711_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='cgpa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
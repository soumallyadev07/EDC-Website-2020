# Generated by Django 3.0.7 on 2020-07-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0005_merge_20200713_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='about',
            field=models.CharField(max_length=200),
        ),
    ]

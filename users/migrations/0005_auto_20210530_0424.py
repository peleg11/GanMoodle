# Generated by Django 3.1.7 on 2021-05-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210530_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='gangrp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

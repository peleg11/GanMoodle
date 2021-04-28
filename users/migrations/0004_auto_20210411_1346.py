# Generated by Django 3.1.7 on 2021-04-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210411_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_address',
        ),
        migrations.AlterField(
            model_name='manager',
            name='muni_cert',
            field=models.FileField(blank=True, null=True, upload_to='municerts'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='police_cert',
            field=models.FileField(blank=True, null=True, upload_to='policerts'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profilepics'),
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-20 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20190819_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.TextField(default='utakpsi@gmail.com', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.TextField(default='John', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.TextField(default='Doe', max_length=20),
        ),
    ]

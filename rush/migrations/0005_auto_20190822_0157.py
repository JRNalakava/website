# Generated by Django 2.2.4 on 2019-08-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0004_auto_20190822_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushee',
            name='random_id',
            field=models.IntegerField(default=12),
        ),
    ]

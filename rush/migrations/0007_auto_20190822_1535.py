# Generated by Django 2.2.4 on 2019-08-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0006_auto_20190822_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushee',
            name='random_id',
            field=models.IntegerField(default=951),
        ),
        migrations.AlterField(
            model_name='rushee',
            name='username',
            field=models.CharField(default='username617', max_length=100),
        ),
    ]

# Generated by Django 2.2.4 on 2019-09-10 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0021_auto_20190909_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushee',
            name='random_id',
            field=models.IntegerField(default=541),
        ),
        migrations.AlterField(
            model_name='rushee',
            name='username',
            field=models.CharField(default='username983', max_length=100),
        ),
    ]
# Generated by Django 2.2.4 on 2019-09-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0025_auto_20190910_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rushee',
            name='username',
            field=models.CharField(default='username<django.db.models.fields.IntegerField>', max_length=100),
        ),
    ]

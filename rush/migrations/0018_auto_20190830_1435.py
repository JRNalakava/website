# Generated by Django 2.2.4 on 2019-08-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_profile_votes'),
        ('rush', '0017_auto_20190830_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='rushee',
            name='voters',
            field=models.ManyToManyField(to='mysite.Profile'),
        ),
        migrations.AlterField(
            model_name='rushee',
            name='random_id',
            field=models.IntegerField(default=530),
        ),
        migrations.AlterField(
            model_name='rushee',
            name='username',
            field=models.CharField(default='username787', max_length=100),
        ),
    ]

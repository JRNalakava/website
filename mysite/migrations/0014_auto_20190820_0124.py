# Generated by Django 2.2.4 on 2019-08-20 06:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20190820_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/texasakpsi/image/upload/v1566281324/profile_pics/blank-profile-picture_twrtwg.png', max_length=255, verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='ProfilePic',
        ),
    ]

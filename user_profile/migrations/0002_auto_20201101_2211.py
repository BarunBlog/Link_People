# Generated by Django 3.1.2 on 2020-11-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='User_image',
            field=models.ImageField(default=1, upload_to='profile_pic/'),
            preserve_default=False,
        ),
    ]

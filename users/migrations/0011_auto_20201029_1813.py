# Generated by Django 3.1.2 on 2020-10-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201029_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/thumbnail/'),
        ),
    ]

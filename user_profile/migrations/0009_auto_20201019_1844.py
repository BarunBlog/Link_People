# Generated by Django 3.1.2 on 2020-10-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20201019_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='End_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='Start_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]

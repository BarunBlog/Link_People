# Generated by Django 3.1.2 on 2020-10-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201022_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_posted_job',
            field=models.BooleanField(default=False),
        ),
    ]

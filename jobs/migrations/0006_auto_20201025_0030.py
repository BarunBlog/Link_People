# Generated by Django 3.1.2 on 2020-10-24 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_applicationmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationmodel',
            old_name='Author_id',
            new_name='Job_id',
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-23 14:00

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostJobModel',
            fields=[
                ('Job_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Job_title', models.CharField(max_length=150)),
                ('Company', models.CharField(max_length=150)),
                ('Job_location', models.CharField(max_length=250)),
                ('Employee_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('self-employed', 'Self-employed'), ('internship', 'Internship'), ('seasonal', 'Seasonal')], max_length=20)),
                ('Date_posted', models.DateField(default=django.utils.timezone.now)),
                ('Is_active', models.BooleanField(default=True)),
                ('Is_approved', models.BooleanField(default=False)),
                ('Description', models.TextField()),
                ('Add_skills', models.TextField()),
                ('Email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-31 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('u_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('User_image', models.ImageField(blank=True, null=True, upload_to='profile_pic/')),
                ('Headline', models.CharField(max_length=50)),
                ('Current_position', models.CharField(blank=True, max_length=100)),
                ('Summary', models.TextField(blank=True)),
                ('School_or_College_or_University', models.CharField(max_length=250)),
                ('Degree', models.CharField(max_length=250)),
                ('Field_of_study', models.CharField(max_length=250)),
                ('Education_Start_year', models.DateField()),
                ('Education_End_year', models.DateField()),
                ('Experience_Title', models.CharField(blank=True, max_length=250)),
                ('Employee_type', models.CharField(blank=True, choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('self-employed', 'Self-employed'), ('internship', 'Internship'), ('seasonal', 'Seasonal')], max_length=20)),
                ('Company', models.CharField(blank=True, max_length=250)),
                ('Start_year', models.DateField(blank=True, null=True)),
                ('End_year', models.DateField(blank=True, null=True)),
                ('Skill', models.TextField(blank=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

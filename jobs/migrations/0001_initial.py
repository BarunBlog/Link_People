# Generated by Django 3.1.2 on 2020-10-26 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('Is_approved', models.BooleanField(default=False)),
                ('Description', models.TextField()),
                ('Add_skills', models.TextField()),
                ('Job_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=150)),
                ('Applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.postjobmodel')),
            ],
        ),
    ]

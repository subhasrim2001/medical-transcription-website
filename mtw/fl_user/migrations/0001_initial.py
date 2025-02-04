# Generated by Django 3.0.3 on 2021-05-27 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctors_name', models.CharField(max_length=100)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('turn_around_time_hr', models.IntegerField()),
                ('audio_name', models.CharField(max_length=100)),
                ('audio_file', models.FileField(blank=True, upload_to='')),
                ('is_asigned', models.BooleanField(default=False)),
                ('transcription_completed', models.BooleanField(default=False)),
                ('QA_passed', models.BooleanField(default=False)),
                ('Doctor_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('assign_first_level_user', models.ForeignKey(limit_choices_to={'user_designation': 'first level user'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2021-05-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fl_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_status',
            name='transcription_completed',
            field=models.BooleanField(default=False),
        ),
    ]

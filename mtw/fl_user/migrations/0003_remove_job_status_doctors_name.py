# Generated by Django 3.0.3 on 2021-05-27 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fl_user', '0002_auto_20210527_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_status',
            name='Doctors_name',
        ),
    ]

# Generated by Django 4.2.6 on 2023-12-25 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodeChecker', '0017_task_completed_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_completed',
            name='task_title',
        ),
    ]

# Generated by Django 4.2.6 on 2023-12-25 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CodeChecker', '0016_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_completed',
            name='task_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CodeChecker.task'),
        ),
    ]

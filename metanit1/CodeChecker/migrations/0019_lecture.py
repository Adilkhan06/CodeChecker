# Generated by Django 4.2.6 on 2023-12-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeChecker', '0018_remove_task_completed_task_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('assignment_link', models.URLField()),
            ],
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-25 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CodeChecker', '0015_remove_customuser_tasks_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_id', models.TextField(blank=True, null=True)),
                ('Customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
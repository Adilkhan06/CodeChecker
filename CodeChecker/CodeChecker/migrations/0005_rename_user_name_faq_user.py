# Generated by Django 4.2.7 on 2023-12-21 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodeChecker', '0004_alter_faq_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='user_name',
            new_name='user',
        ),
    ]
# Generated by Django 5.0.1 on 2024-03-03 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectfiles', '0021_task_doer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='doer',
            new_name='user',
        ),
    ]
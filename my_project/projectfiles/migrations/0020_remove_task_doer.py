# Generated by Django 5.0.1 on 2024-03-03 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectfiles', '0019_task_doer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='doer',
        ),
    ]
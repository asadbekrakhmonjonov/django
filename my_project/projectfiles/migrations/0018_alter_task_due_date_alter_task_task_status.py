# Generated by Django 5.0.1 on 2024-02-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectfiles', '0017_remove_task_day_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Incomplete', 'Incomplete')], max_length=200, null=True),
        ),
    ]

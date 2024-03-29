# Generated by Django 5.0.1 on 2024-02-25 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectfiles', '0015_remove_tasks_doer_remove_tasks_tags_delete_userinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200, null=True)),
                ('task_status', models.IntegerField(choices=[('Completed', 'Completed'), ('Incomplete', 'Incomplete')], null=True)),
                ('day', models.IntegerField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], null=True)),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectfiles', '0007_data_delete_userregistration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200, null=True)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=200, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Incomplete', 'Incomplete')], max_length=200, null=True)),
            ],
        ),
    ]

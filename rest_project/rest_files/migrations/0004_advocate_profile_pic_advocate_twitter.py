# Generated by Django 5.0.1 on 2024-03-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_files', '0003_advocate_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='profile_pic',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='advocate',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]

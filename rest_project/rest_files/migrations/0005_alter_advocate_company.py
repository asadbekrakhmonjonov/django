# Generated by Django 5.0.1 on 2024-03-18 04:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_files', '0004_advocate_profile_pic_advocate_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_files.company'),
        ),
    ]

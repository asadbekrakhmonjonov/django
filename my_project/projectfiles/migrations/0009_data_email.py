# Generated by Django 5.0.1 on 2024-02-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectfiles', '0008_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]

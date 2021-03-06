# Generated by Django 3.1.4 on 2021-12-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20211217_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]

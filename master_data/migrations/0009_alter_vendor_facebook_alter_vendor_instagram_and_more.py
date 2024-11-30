# Generated by Django 5.1.3 on 2024-12-01 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0008_alter_vendorgallery_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(
                '^[0-9a-zA-Z-_@.,]*$', 'Only alphanumeric characters, dot (.), comma (,), at symbol (@) and minus (-) are allowed.')]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(
                '^[0-9a-zA-Z-_@.,]*$', 'Only alphanumeric characters, dot (.), comma (,), at symbol (@) and minus (-) are allowed.')]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='tiktok',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(
                '^[0-9a-zA-Z-_@.,]*$', 'Only alphanumeric characters, dot (.), comma (,), at symbol (@) and minus (-) are allowed.')]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='youtube',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(
                '^[0-9a-zA-Z-_@.,]*$', 'Only alphanumeric characters, dot (.), comma (,), at symbol (@) and minus (-) are allowed.')]),
        ),
    ]
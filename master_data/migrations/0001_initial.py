# Generated by Django 5.1.3 on 2024-11-26 20:21

import master_data.models.vendor_category
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VendorCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to=master_data.models.vendor_category.vendor_category_icon_paths)),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'master_vendor_category',
                'get_latest_by': ['-created_at'],
            },
        ),
    ]

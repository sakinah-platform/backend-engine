# Generated by Django 5.1.3 on 2024-11-30 21:46

import django.db.models.deletion
import master_data.models.vendor
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('about', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('tiktok', models.CharField(blank=True, max_length=100)),
                ('youtube', models.CharField(blank=True, max_length=100)),
                ('profile_image', models.ImageField(blank=True, upload_to=master_data.models.vendor.vendor_profile_images)),
                ('availability', models.BooleanField(default=True)),
                ('visibility', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='public')),
                ('deleted_flag', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master_data.vendorcategory')),
            ],
            options={
                'db_table': 'vendor',
                'get_latest_by': ['-created_at'],
            },
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-01 17:02

import django.core.validators
import master_data.models.vendor_gallery
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0006_vendor_height_field_vendor_width_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorgallery',
            name='image',
            field=models.ImageField(upload_to=master_data.models.vendor_gallery.vendor_galleries, validators=[
                                    django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]

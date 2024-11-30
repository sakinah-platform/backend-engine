# Generated by Django 5.1.3 on 2024-12-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0011_remove_vendorschedule_deleted_flag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorpackage',
            name='deleted_flag',
        ),
        migrations.AddField(
            model_name='vendorpackage',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendorpackage',
            name='restored_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendorpackage',
            name='transaction_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]

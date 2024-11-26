from django.db import models

from master_data.utility.media_utility import vendor_category_icon_paths


# Create your models here.
class VendorCategory(models.Model):

    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    icon = models.ImageField(upload_to=vendor_category_icon_paths, null=False, blank=False)
    deleted_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "master_vendor_category"
        get_latest_by = ["-created_at"]

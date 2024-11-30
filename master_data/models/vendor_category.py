from django.db import models
from django_softdelete.models import SoftDeleteModel

from os import path

from master_data.utility.media_utility import rel_path


def vendor_category_icon_paths(instance, curr_file):
    _, ext = path.splitext(curr_file)
    assigned_filename: str = instance.name.replace(' ', '')

    return rel_path('vendor_category_icons', assigned_filename, ext)

# Create your models here.


class VendorCategory(SoftDeleteModel):

    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    icon = models.ImageField(upload_to=vendor_category_icon_paths,
                             null=False,
                             blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "master_vendor_category"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return self.name

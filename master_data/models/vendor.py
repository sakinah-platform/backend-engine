from django.db import models

from master_data.utility.media_utility import vendor_profile_images
from master_data.models.vendor_category import VendorCategory


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_flag=False)


class Vendor(models.Model):

    class Visibility(models.TextChoices):
        PRIVATE = 'private'
        PUBLIC = 'public'

    name = models.CharField(max_length=100,
                            unique=True,
                            blank=False,
                            null=False)
    description = models.TextField(blank=False, null=False)
    about = models.TextField(blank=False, null=False)
    category = models.ForeignKey(VendorCategory,
                                 on_delete=models.PROTECT,
                                 blank=False,
                                 null=False)
    email = models.EmailField(blank=False, null=False)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    tiktok = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to=vendor_profile_images,
                                      blank=True)
    availability = models.BooleanField(default=True)
    visibility = models.CharField(choices=Visibility,
                                  default=Visibility.PUBLIC)
    deleted_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:

        db_table = "master_vendors"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return self.name

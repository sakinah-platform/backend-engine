from django.db import models
from django.core.validators import FileExtensionValidator

from master_data.utility.media_utility import vendor_profile_images, ALLOWED_IMAGE_EXTENSIONS
from master_data.models.base import BaseModelManager
from master_data.models.vendor_category import VendorCategory


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
    width_field = models.IntegerField(default=200)
    height_field = models.IntegerField(default=200)
    profile_image = models.ImageField(upload_to=vendor_profile_images,
                                      width_field='width_field',
                                      height_field='height_field',
                                      validators=[FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS)],
                                      blank=True)
    availability = models.BooleanField(default=True)
    visibility = models.CharField(choices=Visibility,
                                  default=Visibility.PUBLIC)
    deleted_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:

        db_table = "master_vendor"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return self.name

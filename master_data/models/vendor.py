from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator
from django_softdelete.models import SoftDeleteModel
from os import path

from master_data.utility.media_utility import rel_path, ALLOWED_IMAGE_EXTENSIONS
from master_data.models.vendor_category import VendorCategory
from master_data.models.city import City

alphanumeric_validator = RegexValidator(r'^[0-9a-zA-Z-_@.,]*$',
                                        'Only alphanumeric characters, dot (.), comma (,), at symbol (@) and minus (-) are allowed.')


def vendor_profile_images(instance, curr_file):
    _, ext = path.splitext(curr_file)
    assigned_filename: str = instance.name.replace(' ', '')

    return rel_path('vendor_profile_images', assigned_filename, ext)


class Vendor(SoftDeleteModel):

    class Visibility(models.TextChoices):
        PRIVATE = 'private'
        PUBLIC = 'public'

    name = models.CharField(max_length=100,
                            unique=True,
                            blank=False,
                            null=False)
    description = models.TextField(blank=False, null=False)
    address = models.TextField(blank=True, null=False)
    city = models.ForeignKey(City,
                             on_delete=models.PROTECT,
                             blank=False,
                             null=False)
    about = models.TextField(blank=False, null=False)
    category = models.ForeignKey(VendorCategory,
                                 on_delete=models.PROTECT,
                                 blank=False,
                                 null=False)
    email = models.EmailField(blank=False, null=False)
    facebook = models.CharField(max_length=100, blank=True, validators=[alphanumeric_validator])
    instagram = models.CharField(max_length=100, blank=True, validators=[alphanumeric_validator])
    tiktok = models.CharField(max_length=100, blank=True, validators=[alphanumeric_validator])
    youtube = models.CharField(max_length=100, blank=True, validators=[alphanumeric_validator])
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "vendor"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return self.name

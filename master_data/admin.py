from django.contrib import admin

from master_data.models.city import City
from master_data.models.vendor_category import VendorCategory
from master_data.models.vendor_gallery import VendorGallery
from master_data.models.vendor_package import VendorPackage
from master_data.models.vendor_schedule import VendorSchedule
from master_data.models.vendor import Vendor


# Register your models here.
@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'icon', 'created_at', 'updated_at')
    search_fields = ['id', 'name', 'description']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ['id', 'name', 'description']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'name',
                    'description',
                    'about',
                    'category',
                    'email',
                    'facebook',
                    'instagram',
                    'tiktok',
                    'youtube',
                    'profile_image',
                    'availability',
                    'visibility',
                    'created_at',
                    'updated_at')
    search_fields = ['id',
                     'name',
                     'category',
                     'availability',
                     'visibility']


@admin.register(VendorGallery)
class VendorGalleryAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'image',
                    'vendor',
                    'created_at',
                    'updated_at')
    search_fields = ['id',
                     'vendor']


@admin.register(VendorPackage)
class VendorPackageAdmin(admin.ModelAdmin):

    list_display = ('id',
                    'name',
                    'description',
                    'vendor',
                    'created_at',
                    'updated_at')
    search_fields = ['id',
                     'name',
                     'vendor']


@admin.register(VendorSchedule)
class VendorScheduleAdmin(admin.ModelAdmin):

    list_display = ('vendor',
                    'day',
                    'start_time',
                    'end_time',
                    'created_at',
                    'updated_at')
    search_fields = ['vendor',
                     'day']

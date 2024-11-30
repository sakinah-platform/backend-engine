from django.contrib import admin

from master_data.models.vendor_category import VendorCategory
from master_data.models.vendor_galleries import VendorGallery
from master_data.models.vendor import Vendor


# Register your models here.
@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'icon', 'created_at', 'updated_at')
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

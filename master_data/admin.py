from django.contrib import admin

from master_data.models import VendorCategory


# Register your models here.
@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'icon', 'created_at', 'updated_at')
    search_fields = ['id', 'name', 'description']

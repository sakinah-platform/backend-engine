from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Min
from django.test import TestCase

from master_data.models.vendor_category import VendorCategory
from master_data.models.city import City
from master_data.models.vendor_gallery import VendorGallery
from master_data.models.vendor_package import VendorPackage
from master_data.models.vendor_schedule import VendorSchedule
from master_data.models.vendor import Vendor

from master_data.serializers.vendor_gallery_serializer import VendorGallerySerializer
from master_data.serializers.vendor_package_serializer import VendorPackageSerializer
from master_data.serializers.vendor_schedule_serializer import VendorScheduleSerializer
from master_data.serializers.vendor_serializer import VendorSerializer, VendorListSerializer

from backend.system_utility.system_constant import MINGGU

import datetime


def dummy_image_file(file_name, content_type):
    small_image = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )
    return SimpleUploadedFile(file_name,
                              small_image,
                              content_type=content_type)


def set_up_all_vendor_resources():
    uploaded = dummy_image_file('small.jpg', 'image/jpeg')
    cat = VendorCategory.objects.create(name='test_cat',
                                        description='test_desc',
                                        icon=uploaded)
    city = City.objects.create(name='Garut', description='test city')
    vendor = Vendor.objects.create(name='test_vendor',
                                   description='test_desc',
                                   about='test_about',
                                   email='test@email.com',
                                   category=cat,
                                   city=city,
                                   profile_image=uploaded)
    VendorGallery.objects.create(image=uploaded,
                                 vendor=vendor)
    VendorPackage.objects.create(name='test_package',
                                 price=1,
                                 vendor=vendor)
    VendorSchedule.objects.create(vendor=vendor,
                                  start_time=datetime.time(6, 0),
                                  end_time=datetime.time(8, 0),
                                  day=MINGGU)


class TestVendorListSerializer(TestCase):
    def setUp(self):
        set_up_all_vendor_resources()

        uploaded = dummy_image_file('small.jpg', 'image/jpeg')
        cat = VendorCategory.objects.get(name='test_cat')
        city = City.objects.get(name='Garut')
        vendor_2 = Vendor.objects.create(name='test_vendor_2',
                                         description='test_desc',
                                         about='test_about',
                                         email='test@email.com',
                                         category=cat,
                                         city=city,
                                         profile_image=uploaded)
        VendorPackage.objects.create(name='test_package_2_1',
                                     price=10,
                                     vendor=vendor_2)
        VendorPackage.objects.create(name='test_package_2_2',
                                     price=1,
                                     vendor=vendor_2)

    def test_vendor_list_serializer_result(self):
        vendors = Vendor.objects.annotate(starting_price=Min('packages__price'))
        vendors_list_serializer = VendorListSerializer(vendors, many=True)
        expected_data_result = [{'id': vendors.first().id,
                                 'name': vendors.first().name,
                                 'profile_image': vendors.first().profile_image.url,
                                 'starting_price': 1
                                 },
                                {'id': vendors.last().id,
                                 'name': vendors.last().name,
                                 'profile_image': vendors.last().profile_image.url,
                                 'starting_price': 1
                                 }]
        self.assertEqual(vendors_list_serializer.data, expected_data_result)


class TestVendorSerializer(TestCase):
    def setUp(self):
        set_up_all_vendor_resources()

    def test_vendor_serializer_result(self):
        vendor = Vendor.objects.get(name='test_vendor')
        vendor_serializer = VendorSerializer(vendor)
        vendor_gallery_serializer = VendorGallerySerializer(vendor.galleries, many=True)
        vendor_package_serializer = VendorPackageSerializer(vendor.packages, many=True)
        vendor_schedule_serializer = VendorScheduleSerializer(vendor.schedules, many=True)
        expected_data_result = {'id': vendor.id,
                                'name': vendor.name,
                                'description': vendor.description,
                                'about': vendor.about,
                                'category': vendor.category.id,
                                'email': vendor.email,
                                'facebook': vendor.facebook,
                                'instagram': vendor.instagram,
                                'tiktok': vendor.tiktok,
                                'youtube': vendor.youtube,
                                'profile_image': vendor.profile_image.url,
                                'availability': vendor.availability,
                                'visibility': vendor.visibility,
                                'galleries': vendor_gallery_serializer.data,
                                'packages': vendor_package_serializer.data,
                                'schedules': vendor_schedule_serializer.data}
        self.assertEqual(vendor_serializer.data, expected_data_result)

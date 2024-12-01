from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.utils import IntegrityError
from django.test import TestCase

from master_data.models.vendor_category import VendorCategory
from master_data.models.vendor_gallery import VendorGallery
from master_data.models.vendor_package import VendorPackage
from master_data.models.vendor_schedule import VendorSchedule, Day
from master_data.models.vendor import Vendor

import datetime


def dummy_image_file():
    small_image = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )
    return SimpleUploadedFile('small.jpg',
                              small_image,
                              content_type='image/jpeg')


class TestVendor(TestCase):

    def setUp(self):
        uploaded = dummy_image_file()
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        Vendor.objects.create(name='test_vendor',
                              description='test_desc',
                              about='test_about',
                              category=cat,
                              profile_image=uploaded)
        Vendor.objects.create(name='test_vendor_del',
                              description='test_desc',
                              about='test_about',
                              category=cat,
                              deleted_flag=True,
                              profile_image=uploaded)

    def test_get_vendor_return_not_soft_deleted_vendor(self):
        vendor = Vendor.objects.get(name='test_vendor')

        self.assertEqual(vendor.name, 'test_vendor')
        with self.assertRaises(Vendor.DoesNotExist):
            Vendor.objects.get(name='test_vendor_del')


class TestVendorGallery(TestCase):

    def setUp(self):
        uploaded = dummy_image_file()
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        vendor = Vendor.objects.create(name='test_vendor',
                                       description='test_desc',
                                       about='test_about',
                                       category=cat,
                                       profile_image=uploaded)
        VendorGallery.objects.create(image=uploaded,
                                     vendor=vendor)
        VendorGallery.objects.create(image=uploaded,
                                     vendor=vendor,
                                     deleted_flag=True)

    def test_vendor_gallery_filepath_appended_shortuuid(self):
        vendor = Vendor.objects.get(name='test_vendor')
        vendor_gallery = VendorGallery.objects.get(vendor=vendor)
        expected_filepath_rgx = r'^\/media\/vendor_galleries\/small_[0-9A-Za-z]{22}.jpg'
        self.assertRegex(vendor_gallery.image.url, expected_filepath_rgx)

    def test_get_vendor_gallery_return_not_soft_deleted_image(self):
        vendor_galleries_count = VendorGallery.objects.count()

        expected_images_count = 1
        self.assertEqual(vendor_galleries_count, expected_images_count)


class TestVendorPackage(TestCase):

    def setUp(self):
        uploaded = dummy_image_file()
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        vendor = Vendor.objects.create(name='test_vendor',
                                       description='test_desc',
                                       about='test_about',
                                       category=cat,
                                       profile_image=uploaded)
        VendorPackage.objects.create(name='test_package',
                                     price=1,
                                     vendor=vendor)
        VendorPackage.objects.create(name='test_package_del',
                                     price=0,
                                     vendor=vendor,
                                     deleted_flag=True)

    def test_vendor_package_price_gte_zero(self):
        vendor = Vendor.objects.get(name='test_vendor')
        with self.assertRaises(IntegrityError):
            VendorPackage.objects.create(name='test_package_1',
                                         price=-1,
                                         vendor=vendor)

    def test_get_vendor_package_return_not_soft_deleted_package(self):
        vendor_package_count = VendorPackage.objects.count()

        expected_package_count = 1
        self.assertEqual(vendor_package_count, expected_package_count)


class TestVendorSchedule(TestCase):

    def setUp(self):
        uploaded = dummy_image_file()
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        vendor = Vendor.objects.create(name='test_vendor',
                                       description='test_desc',
                                       about='test_about',
                                       category=cat,
                                       profile_image=uploaded)
        VendorSchedule.objects.create(vendor=vendor,
                                      start_time=datetime.time(6, 0),
                                      end_time=datetime.time(8, 0),
                                      day=Day.SUNDAY)
        VendorSchedule.objects.create(vendor=vendor,
                                      start_time=datetime.time(8, 0),
                                      end_time=datetime.time(10, 0),
                                      day=Day.SUNDAY,
                                      deleted_flag=True)

    def test_get_vendor_schedule_return_not_soft_deleted_package(self):
        vendor_schedule_count = VendorSchedule.objects.count()

        expected_schedule_count = 1
        self.assertEqual(vendor_schedule_count, expected_schedule_count)

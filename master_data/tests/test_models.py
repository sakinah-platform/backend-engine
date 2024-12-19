from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase

from master_data.models.vendor_category import VendorCategory
from master_data.models.vendor_gallery import VendorGallery
from master_data.models.vendor_package import VendorPackage
from master_data.models.vendor_schedule import VendorSchedule
from master_data.models.vendor import Vendor

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


class TestVendorCategory(TestCase):

    def setUp(self):
        uploaded = dummy_image_file('small.jpg', 'image/jpeg')
        VendorCategory.objects.create(name='test_cat',
                                      description='test_desc',
                                      icon=uploaded)
        VendorCategory.objects.create(name='test_deleted',
                                      description='test_desc',
                                      icon=uploaded).delete()

    def test_get_vendor_category_return_not_soft_deleted_image(self):
        vendor_category_count = VendorCategory.objects.count()

        expected_cat_count = 1
        self.assertEqual(vendor_category_count, expected_cat_count)


class TestVendor(TestCase):

    def setUp(self):
        uploaded = dummy_image_file('small.jpg', 'image/jpeg')
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        Vendor.objects.create(name='test_vendor',
                              description='test_desc',
                              about='test_about',
                              email='test@test.com',
                              category=cat,
                              profile_image=uploaded)
        Vendor.objects.create(name='test_vendor_del',
                              description='test_desc',
                              about='test_about',
                              email='test@test.com',
                              category=cat,
                              profile_image=uploaded).delete()

    def test_get_vendor_return_not_soft_deleted_vendor(self):
        vendor = Vendor.objects.get(name='test_vendor')

        self.assertEqual(vendor.name, 'test_vendor')
        with self.assertRaises(Vendor.DoesNotExist):
            Vendor.objects.get(name='test_vendor_del')

    def test_vendor_profile_image_extension_validation(self):
        cat = VendorCategory.objects.get(name='test_cat')
        uploaded_gif = dummy_image_file('small.gif', 'image/gif')

        vendor = Vendor.objects.create(name='test_vendor_gif',
                                       description='test_desc',
                                       about='test_about',
                                       email='test@test.com',
                                       category=cat,
                                       profile_image=uploaded_gif)
        expected_error_message = 'File extension “gif” is not allowed. Allowed extensions are: jpg, jpeg, png.'
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            vendor.full_clean()

    def test_vendor_alphanumeric_validation(self):
        cat = VendorCategory.objects.get(name='test_cat')
        uploaded = dummy_image_file('small.jpg', 'image/jpeg')
        username_violation = '#invalid-user&'

        vendor_fb = Vendor.objects.create(name='test_vendor_fb',
                                          description='test_desc',
                                          about='test_about',
                                          email='test@test.com',
                                          facebook=username_violation,
                                          category=cat,
                                          profile_image=uploaded)
        vendor_ig = Vendor.objects.create(name='test_vendor_ig',
                                          description='test_desc',
                                          about='test_about',
                                          email='test@test.com',
                                          instagram=username_violation,
                                          category=cat,
                                          profile_image=uploaded)
        vendor_tt = Vendor.objects.create(name='test_vendor_tt',
                                          description='test_desc',
                                          about='test_about',
                                          email='test@test.com',
                                          tiktok=username_violation,
                                          category=cat,
                                          profile_image=uploaded)
        vendor_yt = Vendor.objects.create(name='test_vendor_yt',
                                          description='test_desc',
                                          about='test_about',
                                          email='test@test.com',
                                          youtube=username_violation,
                                          category=cat,
                                          profile_image=uploaded)

        expected_error_message = 'Only alphanumeric characters, dot (.), comma (,), at symbol (@) and minus (-) are allowed.'

        with self.assertRaisesMessage(ValidationError, expected_error_message):
            vendor_fb.full_clean()
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            vendor_ig.full_clean()
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            vendor_tt.full_clean()
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            vendor_yt.full_clean()


class TestVendorGallery(TestCase):

    def setUp(self):
        uploaded = dummy_image_file('small.jpg', 'image/jpeg')
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        vendor = Vendor.objects.create(name='test_vendor',
                                       description='test_desc',
                                       about='test_about',
                                       email='test@test.com',
                                       category=cat,
                                       profile_image=uploaded)
        VendorGallery.objects.create(image=uploaded,
                                     vendor=vendor)
        VendorGallery.objects.create(image=uploaded,
                                     vendor=vendor).delete()

    def test_get_vendor_gallery_return_not_soft_deleted_image(self):
        vendor_galleries_count = VendorGallery.objects.count()

        expected_images_count = 1
        self.assertEqual(vendor_galleries_count, expected_images_count)

    def test_vendor_gallery_extension_validation(self):
        vendor = Vendor.objects.get(name='test_vendor')
        uploaded_gif = dummy_image_file('small.gif', 'image/gif')

        vendor_gallery = VendorGallery.objects.create(image=uploaded_gif,
                                                      vendor=vendor)
        expected_error_message = 'File extension “gif” is not allowed. Allowed extensions are: jpg, jpeg, png.'
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            vendor_gallery.full_clean()


class TestVendorPackage(TestCase):

    def setUp(self):
        uploaded = dummy_image_file('small.jpg', 'image/jpeg')
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        vendor = Vendor.objects.create(name='test_vendor',
                                       description='test_desc',
                                       about='test_about',
                                       email='test@test.com',
                                       category=cat,
                                       profile_image=uploaded)
        VendorPackage.objects.create(name='test_package',
                                     price=1,
                                     vendor=vendor)
        VendorPackage.objects.create(name='test_package_del',
                                     price=0,
                                     vendor=vendor).delete()

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
        uploaded = dummy_image_file('small.jpg', 'image/jpeg')
        cat = VendorCategory.objects.create(name='test_cat',
                                            description='test_desc',
                                            icon=uploaded)
        vendor = Vendor.objects.create(name='test_vendor',
                                       description='test_desc',
                                       about='test_about',
                                       email='test@test.com',
                                       category=cat,
                                       profile_image=uploaded)
        VendorSchedule.objects.create(vendor=vendor,
                                      start_time=datetime.time(6, 0),
                                      end_time=datetime.time(8, 0),
                                      day=MINGGU)
        VendorSchedule.objects.create(vendor=vendor,
                                      start_time=datetime.time(8, 0),
                                      end_time=datetime.time(10, 0),
                                      day=MINGGU).delete()

    def test_get_vendor_schedule_return_not_soft_deleted_package(self):
        vendor_schedule_count = VendorSchedule.objects.count()

        expected_schedule_count = 1
        self.assertEqual(vendor_schedule_count, expected_schedule_count)

    def test_vendor_schedule_duplication_not_allowed_validation(self):
        vendor = Vendor.objects.get(name='test_vendor')
        duplicate_schedule = VendorSchedule.objects.create(vendor=vendor,
                                                           start_time=datetime.time(6, 0),
                                                           end_time=datetime.time(8, 0),
                                                           day=MINGGU)
        expected_error_message = 'Schedule for test_vendor already exists'
        with self.assertRaisesMessage(ValidationError, expected_error_message):
            duplicate_schedule.full_clean()

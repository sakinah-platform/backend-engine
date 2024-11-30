from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from master_data.models.vendor_category import VendorCategory
from master_data.models.vendor import Vendor


class TestVendor(TestCase):

    def setUp(self):
        small_image = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile('small.jpg',
                                      small_image,
                                      content_type='image/jpeg')
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

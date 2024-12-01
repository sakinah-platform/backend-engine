from rest_framework import status
from rest_framework.test import APITestCase

from django.core.files.uploadedfile import SimpleUploadedFile

from master_data.models.vendor_category import VendorCategory
from master_data.models.vendor import Vendor


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
    Vendor.objects.create(name='test_vendor',
                          description='test_desc',
                          about='test_about',
                          email='test@email.com',
                          category=cat,
                          profile_image=uploaded)


class TestVendorHandler(APITestCase):
    vendor_id = 0

    def setUp(self):
        set_up_all_vendor_resources()
        self.vendor_id = Vendor.objects.get(name='test_vendor').id

    def test_get_vendor_is_found(self):
        url = f'/master_data/vendors/{self.vendor_id}/'
        response = self.client.get(url, format='json')

        expected_vendor_name = 'test_vendor'
        expected_vendor_description = 'test_desc'
        expected_vendor_about = 'test_about'
        expected_vendor_email = 'test@email.com'

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], expected_vendor_name)
        self.assertEqual(response.data['description'], expected_vendor_description)
        self.assertEqual(response.data['about'], expected_vendor_about)
        self.assertEqual(response.data['email'], expected_vendor_email)

    def test_get_vendor_is_not_found(self):
        url = '/master_data/vendors/999/'
        response = self.client.get(url, format='json')

        expected_vendor_data = [{'attr': None, 'code': 'not_found', 'detail': 'Not found.'}]

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['errors'], expected_vendor_data)

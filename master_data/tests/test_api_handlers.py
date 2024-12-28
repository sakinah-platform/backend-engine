from rest_framework import status
from rest_framework.test import APITestCase
from django.db.models import OuterRef
from django.core.files.uploadedfile import SimpleUploadedFile

from master_data.models.vendor_category import VendorCategory
from master_data.models.city import City
from master_data.models.vendor import Vendor
from master_data.models.vendor_package import VendorPackage
from master_data.models.package_gallery import PackageGallery

from master_data.serializers.package_gallery_serializer import PackageGallerySerializer


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
    cat_2 = VendorCategory.objects.create(name='test_cat_2',
                                          description='test_desc',
                                          icon=uploaded)
    city = City.objects.create(name='Garut', description='test city')
    city_2 = City.objects.create(name='Tasikmalaya', description='test city')
    vendor = Vendor.objects.create(name='test_vendor',
                                   description='test_desc',
                                   about='test_about',
                                   email='test@email.com',
                                   category=cat,
                                   city=city,
                                   profile_image=uploaded)
    package = VendorPackage.objects.create(name='test_package_2_1',
                                           price=10,
                                           vendor=vendor,
                                           description={'min_package': 100})
    PackageGallery.objects.create(image=uploaded,
                                  package=package)


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

        expected_error = [{'attr': None, 'code': 'not_found', 'detail': 'Not found.'}]

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['errors'], expected_error)

    def test_get_vendor_list(self):
        url = f'/master_data/vendors/'
        response = self.client.get(url, format='json')
        vendor = Vendor.objects.get(name='test_vendor')

        expected_vendor_list = [
            {
                'id': vendor.id,
                'name': vendor.name,
                'profile_image': 'http://testserver' + vendor.profile_image.url,
                'starting_price': 10,
                'city': vendor.city.name,
                'category': vendor.category.name
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_name_vendor_found(self):
        url = f'/master_data/vendors/?search=test_vendor'
        response = self.client.get(url, format='json')
        vendor = Vendor.objects.get(name='test_vendor')

        expected_vendor_list = [
            {
                'id': vendor.id,
                'name': vendor.name,
                'profile_image': 'http://testserver' + vendor.profile_image.url,
                'starting_price': 10,
                'city': vendor.city.name,
                'category': vendor.category.name
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_name_vendor_not_found(self):
        url = f'/master_data/vendors/?search=unknown'
        response = self.client.get(url, format='json')

        expected_vendor_list = []

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_category_vendor_found(self):
        vendor = Vendor.objects.get(name='test_vendor')
        url = f'/master_data/vendors/?category={vendor.category.id}'
        response = self.client.get(url, format='json')

        expected_vendor_list = [
            {
                'id': vendor.id,
                'name': vendor.name,
                'profile_image': 'http://testserver' + vendor.profile_image.url,
                'starting_price': 10,
                'city': vendor.city.name,
                'category': vendor.category.name
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_category_vendor_not_found(self):
        cat = VendorCategory.objects.get(name='test_cat_2')
        url = f'/master_data/vendors/?category={cat.id}'
        response = self.client.get(url, format='json')

        expected_vendor_list = []

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_category_category_not_valid(self):
        url = f'/master_data/vendors/?category=90'
        response = self.client.get(url, format='json')

        expected_error = [{'attr': 'category', 'code': 'invalid_choice', 'detail': 'Select a valid choice. That choice is not one of the available choices.'}]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], expected_error)

    def test_get_vendor_list_by_city_vendor_found(self):
        vendor = Vendor.objects.get(name='test_vendor')
        url = f'/master_data/vendors/?city={vendor.city.id}'
        response = self.client.get(url, format='json')

        expected_vendor_list = [
            {
                'id': vendor.id,
                'name': vendor.name,
                'profile_image': 'http://testserver' + vendor.profile_image.url,
                'starting_price': 10,
                'city': vendor.city.name,
                'category': vendor.category.name
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_city_vendor_not_found(self):
        city = City.objects.get(name='Tasikmalaya')
        url = f'/master_data/vendors/?city={city.id}'
        response = self.client.get(url, format='json')

        expected_vendor_list = []

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_city_city_not_valid(self):
        url = f'/master_data/vendors/?city=90'
        response = self.client.get(url, format='json')

        expected_error = [{'attr': 'city', 'code': 'invalid_choice', 'detail': 'Select a valid choice. That choice is not one of the available choices.'}]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], expected_error)

    def test_get_vendor_list_by_starting_price_vendor_found(self):
        vendor = Vendor.objects.get(name='test_vendor')
        url = f'/master_data/vendors/?starting_price={vendor.packages.first().price - 1}'
        response = self.client.get(url, format='json')

        expected_vendor_list = [
            {
                'id': vendor.id,
                'name': vendor.name,
                'profile_image': 'http://testserver' + vendor.profile_image.url,
                'starting_price': 10,
                'city': vendor.city.name,
                'category': vendor.category.name
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)

    def test_get_vendor_list_by_starting_price_vendor_not_found(self):
        vendor = Vendor.objects.get(name='test_vendor')
        url = f'/master_data/vendors/?starting_price={vendor.packages.first().price + 1}'
        response = self.client.get(url, format='json')

        expected_vendor_list = []

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_list)


class TestVendorPackageHandler(APITestCase):
    vendor_id = 0
    package_id = 0

    def setUp(self):
        set_up_all_vendor_resources()
        self.vendor_id = Vendor.objects.get(name='test_vendor').id
        self.package_id = VendorPackage.objects.get(vendor=self.vendor_id).id

    def test_get_vendor_package_is_found(self):
        url = f'/master_data/vendors/{self.vendor_id}/packages/{self.package_id}/'
        response = self.client.get(url, format='json')

        expected_vendor_package_name = 'test_package_2_1'
        expected_vendor_package_description = {'min_package': 100}
        expected_vendor_package_price = 10
        expected_vendor_package_terms_and_condition = ''

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], expected_vendor_package_name)
        self.assertEqual(response.data['description'], expected_vendor_package_description)
        self.assertEqual(response.data['price'], expected_vendor_package_price)
        self.assertEqual(response.data['terms_and_condition'], expected_vendor_package_terms_and_condition)

    def test_get_vendor_package_is_not_found(self):
        url = f'/master_data/vendors/{self.vendor_id}/packages/999/'
        response = self.client.get(url, format='json')

        expected_error = [{'attr': None, 'code': 'not_found', 'detail': 'Not found.'}]

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['errors'], expected_error)

    def test_get_vendor_is_not_found(self):
        url = f'/master_data/vendors/999/packages/{self.package_id}/'
        response = self.client.get(url, format='json')

        expected_error = [{'attr': None, 'code': 'not_found', 'detail': 'A vendor with this id does not exist.'}]

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['errors'], expected_error)

    def test_get_vendor_package_list(self):
        url = f'/master_data/vendors/{self.vendor_id}/packages/'
        response = self.client.get(url, format='json')
        packages = VendorPackage.objects.filter(vendor_id=self.vendor_id)

        expected_vendor_package_list = [
            {
                'id': packages.first().id,
                'name': packages.first().name,
                'first_image': {
                    'id': packages.first().galleries.first().id,
                    'image': 'http://testserver' + packages.first().galleries.first().image.url
                },
                'price': packages.first().price,
                'description': packages.first().description,
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_package_list)

    def test_get_vendor_package_list_short_desc_found(self):
        url = f'/master_data/vendors/{self.vendor_id}/packages/?description=100'
        response = self.client.get(url, format='json')
        packages = VendorPackage.objects.filter(vendor_id=self.vendor_id)

        expected_vendor_package_list = [
            {
                'id': packages.first().id,
                'name': packages.first().name,
                'first_image': {
                    'id': packages.first().galleries.first().id,
                    'image': 'http://testserver' + packages.first().galleries.first().image.url
                },
                'price': packages.first().price,
                'description': packages.first().description,
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_package_list)

    def test_get_vendor_package_list_short_desc_not_found(self):
        url = f'/master_data/vendors/{self.vendor_id}/packages/?description=1000'
        response = self.client.get(url, format='json')

        expected_vendor_package_list = []

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], expected_vendor_package_list)

from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from restaurant.serializers import MenuSerialiser
#TestCase class

class MenuItemTest(TestCase):
   def test_get_item(self):
      item = Menu.objects.create(title="IceCream", price=80, inventory=100)
      self.assertEqual(str(item), "IceCream : 80")


class MenuViewTest(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='moses', password='password123')

        # Add test instances of the Menu model using the setup method
        Menu.objects.create(title="Item 1", price=10, inventory=100)
        Menu.objects.create(title="Item 2", price=20, inventory=200)

    def test_getall(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/restaurant/menus/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add assertions to check if the serialized data equals the response
        self.assertEqual(len(response.data), 2)  








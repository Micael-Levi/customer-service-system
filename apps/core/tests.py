from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class UserRegistrationTestCases(APITestCase):
    def setUp(self):
        self.url = reverse("register")
        self.valid_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword123",
            "confirm_password": "newpassword123",
        }
        self.invalid_confirm_password_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword123",
            "confirm_password": "newpassword",
        }

    def test_valid_user_registration(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("user" in response.data)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_invalid_confirm_password_user_registration(self):
        response = self.client.post(self.url, self.invalid_confirm_password_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("Error" in response.data)


class UserLoginTestCases(APITestCase):
    def setUp(self):
        self.url = reverse("login")
        self.user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )

    def test_valid_user_login(self):
        data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("tokens" in response.data)

    def test_invalid_user_login(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("Error" in response.data)


class UserManagementTestCases(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
        )
        self.url = reverse("users")
        url = reverse("login")
        data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        response = self.client.post(url, data)
        self.token = response.data["tokens"]["access"]
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="JWT " + self.token)

    def test_valid_user_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_user_update(self):
        data = {"first_name": "usertest"}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["first_name"] == "usertest")

    def test_valid_user_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_token_user(self):
        self.token = ""
        self.api_authentication()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# from django.test import TestCase
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from rest_framework import status

# class EmployeeAPITest(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='test', password='12345')
#         self.client.login(username='test', password='12345')

#     def test_create_employee(self):
#         data = {
#             "name": "Raj",
#             "email": "raj@test.com"
#         }
#         response = self.client.post('/api/employees/', data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Employee
class EmployeeAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Get JWT token
        response = self.client.post(
            "/api/token/",
            {"username": "testuser", "password": "testpass123"},
            format="json"
        )
        self.token = response.data["access"]

        # Add token to header
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        # Sample employee
        self.employee = Employee.objects.create(
            name="Test User",
            email="test@example.com",
            department="Engineering",
            role="Developer"
        )
    def test_create_employee(self):
        data = {
            "name": "Rajendra Gupta",
            "email": "raj@test.com",
            "department": "HR",
            "role": "Manager"
        }

        response = self.client.post(
            "/api/employees/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_employee_duplicate_email(self):
        data = {
            "name": "Another User",
            "email": "test@example.com",  # already exists
        }

        response = self.client.post(
            "/api/employees/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_list_employees(self):
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("results" in response.data)
    def test_get_single_employee(self):
        response = self.client.get(f"/api/employees/{self.employee.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_invalid_employee(self):
        response = self.client.get("/api/employees/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    def test_update_employee(self):
        data = {
            "name": "Updated Name",
            "email": "updated@test.com"
        }

        response = self.client.put(
            f"/api/employees/{self.employee.id}/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_delete_employee(self):
        response = self.client.delete(
            f"/api/employees/{self.employee.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

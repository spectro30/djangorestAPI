from django.test import TestCase
from .models import Info
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase (TestCase):
    def setUp(self):
        self.info_key = 0
        self.info = Info(key=self.info_key)

    def test_model_can_create_a_Info(self):
        old_count = Info.objects.count()
        self.info.save()
        new_count = Info.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.info_data = {'key': 0 }
        self.response = self.client.post(
            reverse('create'),
            self.info_data,
            format="json")
    def test_api_can_create_a_info(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)



from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import InventoryItem

class InventoryAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.item = InventoryItem.objects.create(name='Test Item', description='Test Description', quantity=10)

    def test_create_item(self):
        url = reverse('inventoryitem-list')
        data = {'name': 'New Item', 'description': 'New Description', 'quantity': 5}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InventoryItem.objects.count(), 2)
        self.assertEqual(InventoryItem.objects.get(name='New Item').description, 'New Description')

    def test_retrieve_item(self):
        url = reverse('inventoryitem-detail', kwargs={'pk': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Item')

    def test_update_item(self):
        url = reverse('inventoryitem-detail', kwargs={'pk': self.item.pk})
        data = {'name': 'Updated Item', 'description': 'Updated Description', 'quantity': 15}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')
        self.assertEqual(self.item.description, 'Updated Description')
        self.assertEqual(self.item.quantity, 15)

    def test_delete_item(self):
        url = reverse('inventoryitem-detail', kwargs={'pk': self.item.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(InventoryItem.objects.filter(pk=self.item.pk).exists())

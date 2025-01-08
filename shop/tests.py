# shop/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Product


class CategoryTests(APITestCase):
    def test_create_category(self):
        url = reverse('category-list')
        data = {'name': 'Electronics', 'description': 'Electronic products'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', description='Electronic products')

    def test_create_product(self):
        url = reverse('product-list')
        data = {'name': 'Laptop', 'price': '1000.00', 'category': self.category.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product(self):
        product = Product.objects.create(name='Laptop', price='1000.00', category=self.category)
        url = reverse('product-detail', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

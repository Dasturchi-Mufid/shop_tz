from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Product,CustomUser


class CategoryTests(APITestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', 
            password='testpassword', 
            first_name='Test', 
            last_name='User',
            phone_number='1234567890'
        )
        
        self.token_url = reverse('token_obtain_pair')
        response = self.client.post(self.token_url, {'email': 'testuser@example.com', 'password': 'testpassword'}, format='json')
        
        self.token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_category(self):
        url = reverse('category-list')
        data = {'name': 'Electronics', 'description': 'Electronic products'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_category(self):
        category = Category.objects.create(name='Electronics', description='Electronic products')

        url = reverse('category-detail', args=[category.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProductTests(APITestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com', 
            password='testpassword', 
            first_name='Test', 
            last_name='User',
            phone_number='1234567890'
        )
        
        self.token_url = reverse('token_obtain_pair')
        response = self.client.post(self.token_url, {'email': 'testuser@example.com', 'password': 'testpassword'}, format='json')
        
        self.token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.category = Category.objects.create(name='Electronics', description='Electronic products')

    def test_create_product(self):
        url = reverse('product-list')
        data = {'name': 'Laptop', 'price': 1000.00, 'category': self.category.id}
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product(self):
        product = Product.objects.create(name='Laptop', price='1000.00', category=self.category)

        url = reverse('product-detail', args=[product.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

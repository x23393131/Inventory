from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=9.99,
            quantity=10,
            created_by=test_user
        )

    def test_product_content(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(str(product), 'Test Product')

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product List')
        self.assertTemplateUsed(response, 'inventory/list.html')

    def test_product_create_view(self):
        response = self.client.post(reverse('product_create'), {
            'name': 'New Product',
            'description': 'New Description',
            'price': 19.99,
            'quantity': 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.last().name, 'New Product')
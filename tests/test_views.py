from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from inventory.models import Product  # Absolute import

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.product = Product.objects.create(
            name='Existing Product',
            price=15.99,
            quantity=5,
            created_by=self.user
        )
        self.client.login(username='testuser', password='12345')

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Existing Product')
        self.assertTemplateUsed(response, 'inventory/list.html')

    def test_product_create_view(self):
        response = self.client.post(reverse('product_create'), {
            'name': 'New Product',
            'description': 'New Description',
            'price': 19.99,
            'quantity': 5
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.last().name, 'New Product')
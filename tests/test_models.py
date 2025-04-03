from django.test import TestCase
from django.contrib.auth.models import User
from inventory.models import Product  # Absolute import

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            username='testuser', 
            password='12345'
        )
        cls.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=9.99,
            quantity=10,
            created_by=cls.test_user
        )

    def test_product_content(self):
        product = Product.objects.get(id=self.product.id)  # Use the created product's ID
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(str(product), 'Test Product')
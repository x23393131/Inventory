import pytest
from django.contrib.auth import get_user_model
from inventory.models import Product

User = get_user_model()

@pytest.mark.django_db
class TestProductModel:
    def test_product_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        product = Product.objects.create(
            name='Test Product',
            price=9.99,
            quantity=10,
            created_by=user
        )
        assert product.name == 'Test Product'
        assert str(product) == 'Test Product'
import pytest
from django.contrib.auth import get_user_model
# from inventory.models import Product
from inventory.models import Product


User = get_user_model()

@pytest.mark.django_db
class TestProductModel:
    def test_product_creation(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='12345')
        
        # Create a product
        product = Product.objects.create(
            name='Test Product',
            price=9.99,
            quantity=10,
            created_by=user
        )
        
        # Test if the product is created properly
        assert product.name == 'Test Product'
        assert str(product) == 'Test Product'

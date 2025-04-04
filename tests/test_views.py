import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from inventory.models import Product

User = get_user_model()

@pytest.mark.django_db
class TestProductViews:
    def test_product_list_view(self, client):
        user = User.objects.create_user(username='testuser', password='12345')
        Product.objects.create(
            name='Test Product',
            price=9.99,
            quantity=10,
            created_by=user
        )
        client.login(username='testuser', password='12345')
        response = client.get(reverse('product_list'))
        assert response.status_code == 200
        assert 'Test Product' in str(response.content)
from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class ProductModelTests(TestCase):
    def test_str_product(self):
        category = Category.objects.create(name="Pruebas")
        product = Product.objects.create(
            category=category,
            name="Producto Test",
            sku="TEST-001",
            quantity=5,
            price=10000,
            description="Desc de prueba",
        )
        self.assertEqual(str(product), "Producto Test (TEST-001)")


class HomeViewTests(TestCase):
    def test_home_status_code(self):
        response = self.client.get(reverse('almacen:home'))
        self.assertEqual(response.status_code, 200)

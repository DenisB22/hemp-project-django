from django.test import TestCase
from django.test import TestCase
from final_project.store.models import Product


class TestModels(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(
            product_name='Product 1',

        )

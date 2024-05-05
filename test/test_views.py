from django.test import TestCase
from restaurant.models import Menu


class MenuViewTes(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(title="Pasta", price=5.99, inventory=100)

        

    def test_get_all(self):
        self.assertEqual(str(self.menu), "Pasta : 5.99")

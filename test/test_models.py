from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_menu(self):
        item = Menu.objects.create(title='Pasta', price=5.99)
        self.assertEqual(str(item), "Pasta : 5.99")
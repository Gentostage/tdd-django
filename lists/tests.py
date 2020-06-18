from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


# Create your tests here.
class SomeTest(TestCase):
    '''Тест на токсичность'''
    
    def test_root_url_resolves_to_home_page(self):
        '''Тест корневого url'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
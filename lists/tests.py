from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


# Create your tests here.
class SomeTest(TestCase):
    '''Тест на токсичность'''
    
    def test_root_url_resolves_to_home_page(self):
        '''Тест корневого url'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        '''проверка на првильный html домашней страницы'''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
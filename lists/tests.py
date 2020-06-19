from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


# Create your tests here.
class SomeTest(TestCase):
    '''Тест на токсичность'''
    
    def test_uses_home_template(self):
        '''Тест шаблона домашней страницы'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        '''Тест сохранение пост запроса'''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
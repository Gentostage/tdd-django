from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item


# Create your tests here.
class SomeTest(TestCase):
    '''Тест на токсичность'''
    
    def test_uses_home_template(self):
        '''Тест шаблона домашней страницы'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        '''Тест сохранение пост запроса'''
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        
    def test_redirect_after_post(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],'/lists/single-lice-in-world/')
    
    def test_only_saved_item_when_necessary(self):
        '''Сохраняет элементы только когда нужно'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    '''Тест модели списка'''

    def test_save_and_retrieving_items(self):
        '''Тест сохраннение и получение элементов списка'''
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        secomd_saved_item = saved_item[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(secomd_saved_item.text, 'Item the second')


class ListViewTest(TestCase):
    '''Тест предоставления списка'''

    def test_uses_list_tempalte(self):
        '''Тест на использованеи списка шаблона'''

        response = self.client.get('/lists/single-lice-in-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_dispaly_all_items(self):
        '''Тест на отабражения все элемента списка'''

        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/single-lice-in-world/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')

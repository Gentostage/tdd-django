from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisionTest(unittest.TestCase):

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''Демонтаж'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_laster(self):
        '''Начало теста'''

        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        headr_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', headr_text)

        inputbox = self.browser.find_elements_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Купить павлиньи перья')
        time.sleep(1)

        table = self.browser.find_elements_by_id('id_list_table')
        rows = table.find_elements_by_id('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows)
        )
        
        self.fail('Тест Закончен')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
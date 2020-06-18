from selenium import webdriver
import unittest

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
        self.fail('Тест Закончен')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
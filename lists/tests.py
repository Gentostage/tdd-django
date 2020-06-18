from django.test import TestCase

# Create your tests here.
class SomeTest(TestCase):
    '''Тест на токсичность'''

    def test_bad_case(self):
        self.assertEqual(1+1, 3)
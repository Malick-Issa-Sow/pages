from django.test import TestCase # au cas ou j'utilise  de base de donnéé
from django.test import SimpleTestCase #je l'utilise car je n'utilise pas de base de donnéé
# Create your tests here.
# pages/tests.py

class SimpleTests(SimpleTestCase):
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
	def test_about_page_status_code(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code, 200)
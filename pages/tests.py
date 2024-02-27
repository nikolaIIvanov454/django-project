from django.test import TestCase


# Create your tests here.

class HomePageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

class AboutPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about-me/')
        self.assertEqual(response.status_code, 200)

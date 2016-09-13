from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from .views import home


class HomePageTest(TestCase):

        def setUp(self):
            self.factory = RequestFactory()

        def test_home_page_html(self):
            request = self.factory.get(reverse('home-page'))
            response = home(request)
            self.assertIn(b'<h1>Welcome to Addressbook</h1>', response.content)

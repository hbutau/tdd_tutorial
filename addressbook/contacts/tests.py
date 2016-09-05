from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from .views import Home


class HomePageTest(TestCase):

        def setUp(self):
            self.factory = RequestFactory()

        def test_home_page_html(self):
            request = self.factory.get(reverse('home_page'))
            response = Home.as_view()(request)
            self.assertIn('<title>AdressBook</title>', response.content.decode(
                'utf8'))

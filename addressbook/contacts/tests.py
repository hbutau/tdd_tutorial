from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from .views import Home


class HomePageTest(TestCase):

        def setUp(self):
            self.factory = RequestFactory()

        def test_home_page_html(self):
            request = self.factory.get('/')
            response = Home.as_view()(request)
            self.assertEqual('home.html', response.template_name[0])
        # def test_home_page_html(self):
        #     request = self.factory.get(reverse('home-page'))
        #     response = home(request)
        #     self.assertIn(b'<h1>Welcome to Addressbook</h1>', response.content)

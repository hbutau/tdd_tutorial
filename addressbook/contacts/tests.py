from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from .views import home# , CreateContactView


class HomePageTest(TestCase):

        def setUp(self):
            self.factory = RequestFactory()

        def test_home_page_html(self):
            request = self.factory.get(reverse('home_page'))
            response = home(request)
            self.assertIn(b'<h1>Welcome to Addressbook</h1>', response.content)
            # self.assertIn('<title>AdressBook</title>', response.content.decode(
            # 'utf8'))
            # self.assertEqual('home.html', response.template_name[0])

        # def test_add_contact_page(self):
        #     request = self.factory.get('contacts-new')
        #     response = CreateContactView.as_view()(request)
        #     self.assertEqual('edit_contact.html', response.template_name[0])

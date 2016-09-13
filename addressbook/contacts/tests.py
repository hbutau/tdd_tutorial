from django.test import TestCase

# Create your tests here.
class Home_Page_Test(TestCase):

    def test_home_page_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn()

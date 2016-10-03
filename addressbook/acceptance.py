

from selenium import  webdriver
import unittest
# driver = webdriver.Chrome()
# driver.get("http://localhost:8000")
# assert "It worked!" in driver.find_element_by_tag_name('h1').text
class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("localhost:8000")
        self.assertTrue("Welcome to Addressbook" == self.driver.find_element_by_tag_name('h1').text)
        # self.fail('Finish the Tests!')


# class IntergrationTests(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def tearDown(self):
#         self.driver.quit()

#     def test_add_contact(self):
#         self.driver.get('localhost:8000/new')
#         self.assertIn('Add Contact', self.driver.find_element_by_tag_name('h1').text)
#         # self.driver.find_element_by_link_text('add contact').click()

#         self.driver.find_element_by_id('id_first_name').send_keys('test')
#         self.driver.find_element_by_id('id_last_name').send_keys('contact')
#         self.driver.find_element_by_id('id_email').send_keys('test@example.com')

#         self.driver.find_element_by_name("save").click()
#         # self.assertEqual(
#         #     self.driver.find_elements_by_css_selector('.contact')[-4].text,
#         #     'test contact'
#         # )

if __name__ == '__main__':
    unittest.main()

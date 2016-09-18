#!/usr/bin/env python3

import unittest
from selenium import webdriver


class Django_Page_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('localhost:8000')

    def teardown(self):
        self.driver.quit()

    def test_django_page(self):
        self.assertTrue(
            'Welcome to Addressbook' == self.driver.find_element_by_tag_name(
                'h1').text
        )


# class IntergrationTests(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def tearDown(self):
#         self.driver.quit()

#     def test_add_contact(self):
#         self.driver.get('localhost:8000/new')
#         self.assertIn('Add Contact', self.driver.find_element_by_tag_name('h1').text)
#         self.driver.find_element_by_link_text('add contact').click()

#         self.driver.find_element_by_id('id_first_name').send_keys('test')
#         self.driver.find_element_by_id('id_last_name').send_keys('contact')
#         self.driver.find_element_by_id('id_email').send_keys('test@example.com')
#         self.driver.find_element_by_name("save").click()
        # self.assertEqual(self.driver.find_elements_by_css_selector('.contact')[-4].text,
        # 'test contact')

if __name__ == '__main__':
    unittest.main()

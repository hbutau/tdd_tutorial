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
        self.assertTrue('Welcome to Addressbook' == self.driver.find_element_by_tag_name('h1').text)

if __name__ == '__main__':
    unittest.main()

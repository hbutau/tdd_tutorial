#!/usr/bin/env python3

import unittest
from selenium import webdriver


class Django_Page_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_django_page(self):
        self.assertEquals('Congratulations on your first Django-powered page.',
            self.driver.find_element_by_tag_name('h2').text)

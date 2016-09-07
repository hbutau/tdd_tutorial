#!/usr/bin/env python3

import unittest
from selenium import webdriver


class HomePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("localhost:8000")
        self.assertIn("AdressBook", self.driver.title)
        self.fail('Finish the Tests!')

if __name__ == '__main__':
    unittest.main()

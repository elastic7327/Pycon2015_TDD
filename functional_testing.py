#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        # self.browser.get("http://localhost:7000")
        # self.assertIn("To-Do",  self.browser.title)
        self.fail("finsh the test!")


if __name__ == "__main__":
    unittest.main()

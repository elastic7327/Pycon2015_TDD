#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do",  self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn("To-Do", header.text)
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys("\n")  # this is enterKey
        #
        #
        import time
        time.sleep(3)
        #
        #
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
                '1: Buy peacock feathers',
                [row.text for row in rows]
        )
        #
        self.fail("Finish the test!!")


if __name__ == "__main__":
    unittest.main(warnings='ignore')

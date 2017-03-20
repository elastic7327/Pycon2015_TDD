#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://localhost:7000")
assert "Django" in browser.title


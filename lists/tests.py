from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        exptected_content = render_to_string('home.html')
        self.assertEqual(response.content.decode('utf8'), exptected_content)
        # with open('lists/templates/home.html') as template:
        #    self.assertEqual(response.content.decode('utf8'), template.read())
        self.assertIn("<title>To-Do lists</title>", response.content.decode("utf8"))
        print(response.content)
        self.assertTrue(response.content.strip().startswith(b"<html>"))
        self.assertTrue(response.content.strip().endswith(b"</html>"))

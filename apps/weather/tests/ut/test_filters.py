from django.test import TestCase
from apps.weather.templatetags.custom_filters import uppercase_filter


class UppercaseFilterTest(TestCase):
    def test_uppercase_filter(self):
        result = uppercase_filter("hello")
        self.assertEqual(result, "HELLO")

    def test_uppercase_filter_empty_string(self):
        result = uppercase_filter("")
        self.assertEqual(result, "")


from django.test import TestCase
from apps.weather.form import SearchForm


class SearchFormTest(TestCase):
    def test_search_form_valid(self):
        form = SearchForm(data={'search_bar': 'New York'})

        self.assertTrue(form.is_valid())

    def test_search_form_invalid(self):
        form = SearchForm(data={})

        self.assertFalse(form.is_valid())

    def test_search_form_max_length(self):
        form = SearchForm(data={'search_bar': 'A' * 101})

        self.assertFalse(form.is_valid())



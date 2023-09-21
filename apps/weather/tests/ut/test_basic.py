from django.test import TestCase


class TestBasicCalculations(TestCase):
    def test_basic_sum(self):
        x = 1
        y = 4

        result = x + y

        assert result == 5


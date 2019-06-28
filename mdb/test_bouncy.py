from unittest import  TestCase
from django.test import TestCase
from movies.bouncy_numbers import bouncy_99, decreciente, enlista, creciente


class BouncyTestCase(TestCase):

    def test_648_not_is_decrease_number (self):
        assert not decreciente(648)

    def test_is_a_list_whit_one(self):
        assert isinstance(enlista(1),list)

    def test_141_not_is_increase_number(self):
        assert not creciente(141)

    def test_1587000_is_99_percent_bouncy_number(self):
        assert bouncy_99(0.99) == 1587000

    def test_538_is_50_percent_bouncy_number(self):
        assert bouncy_99(0.99) == 538

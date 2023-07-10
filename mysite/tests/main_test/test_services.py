from unittest import TestCase
from main.services import calc


class ServiceTest(TestCase):

    def test_plus(self):
        result = calc(7, 12, "+")
        self.assertEqual(19, result)

    def test_minus(self):
        result = calc(7, 12, "-")
        self.assertEqual(-5, result)

    def test_umnozhit(self):
        result = calc(7, 12, "*")
        self.assertEqual(84, result)

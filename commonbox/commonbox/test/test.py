import unittest
from django.test import TestCase

class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1


class URLViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/search_result/')
        self.assertEqual(resp.status_code, 200)
        print resp.context

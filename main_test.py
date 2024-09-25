import unittest

class TestTests(unittest.TestCase):
    def test_upper(self) -> None:
        self.assertEqual('foo'.upper(), 'FOO')

from trebuchet import Trebuchet
import unittest

class TrebuchetTests(unittest.TestCase):
    def test_find_first_val(self):
        t = Trebuchet("test.txt")
        first_val  = t.find_first_val("1abc2")
        assert first_val == 1
    def test_find_second_val(self):
        t = Trebuchet("test.txt")
        first_val  = t.find_second_val("1abc2")
        assert first_val == 2

import unittest

from mystring.MyStringUtils import MyStringUtils


class TestStringUtils(unittest.TestCase):

    def test_reverse(self):
        _utils = MyStringUtils()
        self.assertEquals(_utils.reverse("hello"), "olleh")

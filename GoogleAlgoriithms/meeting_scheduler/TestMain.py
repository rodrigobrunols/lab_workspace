import unittest
import Main


class TestMain(unittest.TestCase):

    def test_main(self):
        self.assertEquals(Main.main(), "Hello")

import unittest
from LoginService import LoginService

class TestLoginService(unittest.TestCase):

    def setUp(self):
        self.service = LoginService()

    def testSingleVisitor(self):
        self.service.logVisitor(1)
        self.assertEqual(self.service.getFirstOneTimeVisitor(), 1)

    def testRepeatedVisitorRemoved(self):
        self.service.logVisitor(1)
        self.service.logVisitor(1)
        self.assertEqual(self.service.getFirstOneTimeVisitor(), -1)

    def test_multiple_visitors_order(self):
        self.service.logVisitor(1)
        self.service.logVisitor(2)
        self.service.logVisitor(3)
        self.service.logVisitor(2)
        self.assertEqual(self.service.getFirstOneTimeVisitor(), 1)

    def test_first_visitor_becomes_recurring(self):
        self.service.logVisitor(1)
        self.service.logVisitor(2)
        self.service.logVisitor(1)
        self.assertEqual(self.service.getFirstOneTimeVisitor(), 2)

    def test_no_one_time_visitors(self):
        self.service.logVisitor(1)
        self.service.logVisitor(1)
        self.service.logVisitor(2)
        self.service.logVisitor(2)
        self.assertEqual(self.service.getFirstOneTimeVisitor(), -1)

if __name__ == '__main__':
    unittest.main()

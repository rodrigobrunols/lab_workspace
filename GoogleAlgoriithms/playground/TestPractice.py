import unittest
from LockerSystem import Package, Size


class TestPackage(unittest.TestCase):

    def setUp(self):
        self.package = Package("1", Size.MEDIUM)

    def testGetSize(self):
        self.assertEquals(self.package.size, Size.MEDIUM)


if __name__ == "__main__":
    unittest.main()

from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)



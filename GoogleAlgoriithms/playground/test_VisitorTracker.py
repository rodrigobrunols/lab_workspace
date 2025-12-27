import unittest
from VisitorTracker import VisitorTracker
time
thre

class TestVisitorTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = VisitorTracker()


    def test_single_one_time_visitor(self):
        self.tracker.log_visitor(1)
        self.assertEqual(self.tracker.get_first_onetime_visitor(), 1)

        self.tracker.log_visitor(1)
        self.assertEqual(self.tracker.get_first_onetime_visitor(), -1)

        self.tracker.log_visitor(2)
        self.assertEqual(self.tracker.get_first_onetime_visitor(), 2)
        self.assertEqual(len(self.tracker.visit_counts), 2)



if __name__ == "__main__":
    unittest.main()

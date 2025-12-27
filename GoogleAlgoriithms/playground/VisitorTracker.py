# Millions of customers visit our website every day.
# For, for each customer we have a unique identifier that is the same every time they visit.
from collections import deque, defaultdict, OrderedDict


# We have 2 kinds of customers:.
# Recurrent Visitors that visit more than once and
# OneTime Visitors, who so far have visited the website only #once.
# We want to implement a class that has 2 functionalities:

# - logVisitor(int id)
# - getFirstOneTimeVisitor()

class VisitorTracker:
    def __init__(self):
        self.visit_counts = OrderedDict()

    def log_visitor(self, id):
        self.visit_counts[id] = self.visit_counts.get(id, 0) + 1
        first_key = next(iter(self.visit_counts))
        if self.visit_counts[first_key] != 1:
            self.visit_counts.move_to_end(id, last=False)

        elif self.visit_counts.get(id) > 1:
            self.visit_counts.move_to_end(id)

    def get_first_onetime_visitor(self):
        if self.visit_counts:
            first_key = next(iter(self.visit_counts))
            return first_key if self.visit_counts[first_key] == 1 else -1
        return -1

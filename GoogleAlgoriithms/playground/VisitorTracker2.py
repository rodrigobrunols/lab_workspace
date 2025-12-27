# Millions of customers visit our website every day.
# For, for each customer we have a unique identifier that is the same every time they visit.
from collections import OrderedDict


# We have 2 kinds of customers:.
# Recurrent Visitors that visit more than once and
# OneTime Visitors, who so far have visited the website only #once.
# We want to implement a class that has 2 functionalities:

# - logVisitor(int id)
# - getFirstOneTimeVisitor()

# * O(1) in both operations
# * Follow-up 1:  billions of users
# * Follow-up 2: How would you modify this solution if we needed to get the most recent one-time visitor
# instead of the first one?

class VisitorTracker:
    def __init__(self):
        self.visit_counts = OrderedDict()

    def log_visitor(self, id):
        self.visit_counts[id] = self.visit_counts.get(id, 0) + 1
        if self.visit_counts.get(id) == 1:
            self.visit_counts.move_to_end(id, last=False)
        else:
            self.visit_counts.move_to_end(id)

    def get_last_onetime_visitor(self):
        if self.visit_counts:
            first_key = next(iter(self.visit_counts))
            return first_key if self.visit_counts[first_key] == 1 else -1
        return -1


def main():
    service = VisitorTracker()
    for i in range(1, 4):
        service.log_visitor(i)

    print(service.get_last_onetime_visitor())

    for i in range(2, 4):
        service.log_visitor(i)
    print(service.get_last_onetime_visitor())


if __name__ == "__main__":
    main()
